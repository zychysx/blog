from django.shortcuts import render, HttpResponse
from django.http.response import JsonResponse
from django.core.paginator import Paginator
from django.conf import settings

from utils.forms import WriteForm
from utils.msg_dict import *
from utils.decorator import login_sugar
from .models import ArticleCategory, BlogArticle

# Create your views here.


@login_sugar
def write(request):
    if request.method == "POST":
        if not request.POST.get('blog_text', None):
            return JsonResponse(context_empty, json_dumps_params={'ensure_ascii': False})

        if request.POST.get('article_title', None):
            return JsonResponse(title_empty, json_dumps_params={'ensure_ascii': False})

        if BlogArticle.objects.filter(article_title=request.POST.get('article_title')).exist():
            return JsonResponse(title_exist, json_dumps_params={'ensure_ascii': False})

        data_dict = dict()
        data_dict["article_title"] = request.POST.get('article_title')
        data_dict["article_user"] = request.blog_user
        data_dict["content"] = request.POST.get('blog_text')
        data_dict["privacy"] = int(request.POST.get('privacy', 0))
        data_dict["recommend"] = int(request.POST.get('recommend', 0))
        data_dict["category"] = ArticleCategory.objects.get(pk=request.POST.get('category'))
        obj = BlogArticle(**data_dict)
        obj.save()
        return JsonResponse(success)

    write_form = WriteForm()
    teg_list = ArticleCategory.objects.filter(category_type="2", is_delete=False)
    return render(request, 'write.html', {"write_form": write_form,
                                          "teg_list": teg_list
                                          })


def article_list(request, t=None):
    category_list = ArticleCategory.objects.filter(category_type="2", is_delete=False)
    default_tag_list = ['checkbox_all'] + [i.id for i in category_list]
    tag_list = [i if i == 'checkbox_all' else int(i) for i in request.GET.getlist("category", default_tag_list)]
    filter_list = [i for i in tag_list if isinstance(i, int)]

    if request.GET.get("privacy", False) and hasattr(request.blog_user, 'user_uuid'):
        blog_list = BlogArticle.objects.filter(category__in=filter_list, privacy=True, article_user=request.blog_user,
                                               is_delete=False)
        tag_list.append("privacy")

    elif request.GET.get("recommend", False):
        blog_list = BlogArticle.objects.filter(category__in=filter_list, recommend=True, is_delete=False)
        tag_list.append("recommend")

    else:
        blog_list = BlogArticle.objects.filter(category__in=filter_list, privacy=False, is_delete=False)

    page_num = int(request.GET.get("page_num", 1))
    context = {
        "category_list": category_list,
        "tag_list": tag_list,
    }

    if t == 2:
        blog_list, all_page_num, count_num, has_pre, has_next, page_range = fenye(blog_list,
                                                                                  page_num, settings.LIST_TOW_PAGE_NUM)
    elif t == 3:
        blog_list, all_page_num, count_num, has_pre, has_next, page_range = fenye(blog_list,
                                                                                  page_num, settings.LIST_TOW_PAGE_NUM)
    else:
        blog_list, all_page_num, count_num, has_pre, has_next, page_range = fenye(blog_list,
                                                                                  page_num, settings.LIST_ONE_PAGE_NUM)
    context["blog_list"] = blog_list
    context["all_page_num"] = all_page_num
    context["count_num"] = count_num
    context["has_pre"] = has_pre
    context["has_next"] = has_next
    context["page_range"] = page_range
    context["page_num"] = page_num
    if t == 2:
        return render(request, 'blog-2-column.html', context)
    elif t == 3:
        return render(request, 'blog-3-column.html', context)
    return render(request, 'blog.html', context)


def article_details(request, article_uuid):
    try:
        obj = BlogArticle.objects.get(article_uuid=article_uuid, is_delete=False)
    except BlogArticle.DoesNotExist:
        return HttpResponse('此文章不存在')
    else:
        if obj.privacy and request.blog_user != obj.article_user and request.blog_user.is_super:
            return HttpResponse('没有查看此文章的权限')

    return render(request, 'details.html', {"obj": obj})


def fenye(obj, page_num, page_size):
    paginator = Paginator(obj, page_size)
    obj_list = paginator.page(page_num)
    all_page_num = paginator.num_pages
    count_num = paginator.count
    has_pre = paginator.page(page_num).has_previous()
    has_next = paginator.page(page_num).has_next()
    if all_page_num < 5:
        page_range = paginator.page_range
    else:
        if page_num >= list(paginator.page_range)[-3]:
            page_range = list(paginator.page_range)[-5:]
        elif page_num <= list(paginator.page_range)[2]:
            page_range = list(paginator.page_range)[:5]
        else:
            page_range = list(paginator.page_range)[page_num - 3:page_num + 2]
    return obj_list, all_page_num, count_num, has_pre, has_next, page_range
