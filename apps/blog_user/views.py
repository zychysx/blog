from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password

from utils.verification import verification_sign_up, verification_username_exist
from utils.session import set_session, del_session
from article.models import BlogArticle, ArticleCategory
from utils.msg_dict import *
from .models import BlogUser


# Create your views here.


def index(request, t=None):

    reccent_list = BlogArticle.objects.filter(privacy=False, is_delete=False)[:5]
    category_list = ArticleCategory.objects.filter(category_type="2", is_delete=False)
    popular_list = BlogArticle.objects.filter(privacy=False, is_delete=False).order_by("-read_num")[:5]
    context = {
        "reccent_list": reccent_list,
        "category_list": category_list,
        "popular_list": popular_list
    }
    if t == 2:
        blog_list = BlogArticle.objects.filter(recommend=True, is_delete=False)[:6]
        context["blog_list"] = blog_list
        return render(request, 'index2.html', context)
    elif t == 3:
        blog_list = BlogArticle.objects.filter(recommend=True, is_delete=False)[:4]
        context["blog_list"] = blog_list
        return render(request, 'index3.html', context)
    blog_list = BlogArticle.objects.filter(recommend=True, is_delete=False)[:5]
    context["blog_list"] = blog_list
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

