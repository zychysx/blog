from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password

from utils.verification import verification_sign_up, verification_username_exist
from utils.session import set_session, del_session
from utils.msg_dict import *
from blog_user.models import BlogUser


# Create your views here.


def index(request, t=None):
    if t == 2:
        return render(request, 'index2.html')
    elif t == 3:
        return render(request, 'index3.html')
    return render(request, 'index.html')


def register(request):
    if request.method == "POST":
        data_dict = verification_sign_up(request)
        obj = BlogUser(**data_dict)
        obj.save()
        set_session(request, obj=obj)
        return redirect(request.session['pre_path'])
    return render(request, 'register.html')


def login(request):
    if not request.POST.get('username', None):
        return JsonResponse(name_empty)

    if verification_username_exist(request):
        return JsonResponse(name_exist)

    password = request.POST.get('password', None)
    obj = BlogUser.objects.get(username=request.POST.get('username'))
    if not check_password(password, obj.password):
        return JsonResponse(wrong_n_p)

    set_session(request, obj=obj)
    msg_dict = {'status': 1}
    return JsonResponse(msg_dict)


def logout(request):
    del_session(request)
    return redirect(request.session['pre_path'])

