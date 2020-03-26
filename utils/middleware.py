from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse
from django.conf import settings

from datetime import timedelta, datetime

from blog_user.models import UserLoginIP, BlogUser
from utils.msg_dict import msg_frequency


exclude_path = [
    '/user/register.html',
    '/user/login.html',
]


def handle_frequency(request, user_ip):
    request_time = datetime.now() - timedelta(hours=settings.FREQUENCY_HOUR, minutes=0, seconds=0)
    f_num = UserLoginIP.objects.filter(IP=user_ip, create_time__gte=request_time).order_by('-create_time').count()
    if not request.session.get('username', None):
        if f_num > settings.IP_FREQUENCY_NUM and user_ip not in settings.IP_FREQUENCY_LIST:
            return False
        return True
    if request.session.get('username') not in settings.USER_FREQUENCY_LIST and user_ip not in settings.IP_FREQUENCY_LIST:
        if f_num > settings.USER_FREQUENCY_NUM:
            return False
    return True


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
        if request.session.get('username', None):
            data_dict["user"] = BlogUser.objects.get(username=request.session.get('username'))
        obj = UserLoginIP(**data_dict)
        obj.save()
