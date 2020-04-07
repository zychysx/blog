import functools

from django.shortcuts import redirect


def login_sugar(func):
    @functools.wraps(func)
    def wapper(request, *args, **kwargs):
        if hasattr(request.blog_user, 'user_uuid'):
            return func(request, *args, **kwargs)
        else:
            return redirect('/user/login.html')
    return wapper
