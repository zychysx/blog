from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password

from utils.verification import verification_sign_up, verification_username_exist, verification_user_active
from utils.session import set_session, del_session
from article.models import BlogArticle, ArticleCategory
from utils.decorator import login_sugar
from utils.msg_dict import *
from .models import BlogUser


# Create your views here.


def index(request):
    newest_list = BlogArticle.objects.filter(privacy=False, is_delete=False)[:5]
    recommend_list = BlogArticle.objects.filter(privacy=False, recommend=True, is_delete=False)[:5]
    popular_list = BlogArticle.objects.filter(privacy=False, is_delete=False).order_by("-read_num")[:5]
    one_category_list = ArticleCategory.objects.filter(category_type="1", is_delete=False)
    tow_category_list = ArticleCategory.objects.filter(category_type="2", is_delete=False)
    blog_count = BlogArticle.objects.filter(is_delete=False).count()
    context = {
        "recommend_list": recommend_list,
        "one_category_list": one_category_list,
        "tow_category_list": tow_category_list,
        "popular_list": popular_list,
        "newest_list": newest_list,
        "blog_count": blog_count,
    }
    return render(request, 'index.html', context)


def register(request):
    if request.method == "POST":
        data_dict = verification_sign_up(request)
        obj = BlogUser(**data_dict)
        obj.save()
        set_session(request, obj=obj)
        return redirect(request.session['pre_path'])
    return render(request, 'register.html')


def login(request):
    if request.method == "POST":
        if not request.POST.get('username', None):
            return HttpResponse("必须输入用户名")

        if verification_username_exist(request):
            return HttpResponse("用户名不存在")

        if not verification_user_active(request):
            return HttpResponse("用户被禁止登陆")

        password = request.POST.get('password', None)
        obj = BlogUser.objects.get(username=request.POST.get('username'))
        if not check_password(password, obj.password):
            return HttpResponse("用户名或密码错误")

        set_session(request, obj=obj)
        return redirect(request.session['pre_path'])
    return render(request, 'login.html')


@login_sugar
def logout(request):
    del_session(request)
    return redirect(request.session['pre_path'])

