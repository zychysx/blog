from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse

from .models import Comment
from article.models import BlogArticle
from utils.decorator import login_sugar
from utils.msg_dict import *

# Create your views here.


@login_sugar
def create_comment(request):
    print(request.POST)
    if not request.POST.get("comment_text", None):
        return HttpResponse("评论内容不能为空")
    comment_text = request.POST.get("comment_text", None)
    content_type = request.POST.get("content_type", None)
    object_uuid = request.POST.get("object_uuid", None)

    article_obj = BlogArticle.objects.get(article_uuid=object_uuid)
    Comment.objects.create(
        content_object=article_obj,
        user=request.blog_user,
        text=comment_text
    )
    return redirect(request.session['pre_path'])
