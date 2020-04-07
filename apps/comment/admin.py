import xadmin

from django.contrib import admin

from .models import Comment

# Register your models here.


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["user", "text", "content_type", "update_time", "create_time", "is_delete"]
    search_fields = ["user", "content_type"]  # 搜索字段
    date_hierarchy = "create_time"  # 详细时间分层筛选　
    list_filter = ["user", "content_type"]  # 过滤器
    list_per_page = 50  # 设置每页显示多少条记录，默认是100条
    ordering = ("-create_time",)  # 设置默认排序字段，负号表示降序排序
    list_display_links = ("user",)  # 设置哪些字段可以点击进入编辑界面


@xadmin.sites.register(Comment)
class UserLoginIPXadmin():
    list_display = ["user", "text", "content_type", "update_time", "create_time", "is_delete"]
    search_fields = ["user", "content_type"]  # 搜索字段
    date_hierarchy = "create_time"  # 详细时间分层筛选　
    list_filter = ["user", "content_type"]  # 过滤器
    list_per_page = 50  # 设置每页显示多少条记录，默认是100条
    ordering = ("-create_time",)  # 设置默认排序字段，负号表示降序排序
    list_display_links = ("user",)  # 设置哪些字段可以点击进入编辑界面
