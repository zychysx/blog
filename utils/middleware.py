from django.utils.deprecation import MiddlewareMixin
from django.utils.functional import SimpleLazyObject
from django.contrib.auth.models import AnonymousUser
from django.shortcuts import HttpResponse
from django.utils import timezone
from django.conf import settings

from datetime import timedelta, datetime

from blog_user.models import UserLoginIP, BlogUser
from .msg_dict import msg_frequency


exclude_path = [
    '/user/register.html',
    '/user/login.html',
]


def handle_frequency(request, user_ip):
    request_time = datetime.now(tz=timezone.utc) - timedelta(hours=settings.FREQUENCY_HOUR, minutes=0, seconds=0)
    f_num = UserLoginIP.objects.filter(IP=user_ip, create_time__gte=request_time).order_by('-create_time').count()
    if not hasattr(request.blog_user, 'user_uuid'):
        if f_num > settings.IP_FREQUENCY_NUM and user_ip not in settings.IP_FREQUENCY_LIST:
            return False
        return True
    if request.session.get('user_uuid') not in settings.USER_FREQUENCY_LIST and user_ip not in settings.IP_FREQUENCY_LIST:
        if f_num > settings.USER_FREQUENCY_NUM:
            return False
    return True


def get_user(request):
    user = None
    if request.session.get('user_uuid', None):
        try:
            user = BlogUser.objects.get(user_uuid=request.session.get('user_uuid'))
        except BlogUser.DoesNotExist:
            return None
        return user if user.is_active else None
    return user or AnonymousUser()


class BlogUserMiddleware(MiddlewareMixin):
    def process_request(self, request):
        assert hasattr(request, 'session'), (
            "The Django authentication middleware requires session middleware "
            "to be installed. Edit your MIDDLEWARE%s setting to insert "
            "'django.contrib.sessions.middleware.SessionMiddleware' before "
            "'django.contrib.auth.middleware.AuthenticationMiddleware'."
        ) % ("_CLASSES" if settings.MIDDLEWARE is None else "")
        request.blog_user = SimpleLazyObject(lambda: get_user(request))


class UrlRecordMiddleware(MiddlewareMixin):
    def process_view(self, request, func, *args, **kwargs):
        if request.path.endswith('.html') and request.path not in exclude_path:
            request.session['pre_path'] = request.get_full_path() or '/'
        request.session['pre_path'] = '/'


class IPFrequencyMiddleware(MiddlewareMixin):
    def process_view(self, request, func, *args, **kwargs):
        user_ip = request.META.get('HTTP_X_FORWARDED_FOR') if request.META.get('HTTP_X_FORWARDED_FOR') else request.META.get('REMOTE_ADDR')
        if not handle_frequency(request, user_ip):
            return HttpResponse(msg_frequency)


class IPRecordMiddleware(MiddlewareMixin):
    def process_view(self, request, func, *args, **kwargs):
        data_dict = dict()
        data_dict["IP"] = request.META.get('HTTP_X_FORWARDED_FOR') if request.META.get('HTTP_X_FORWARDED_FOR') else request.META.get('REMOTE_ADDR')
        if hasattr(request.blog_user, 'user_uuid'):
            data_dict["user"] = request.blog_user
        obj = UserLoginIP(**data_dict)
        obj.save()
