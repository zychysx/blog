import xadmin

from django.contrib import admin

from .models import BlogArticle, ArticleCategory

# Register your models here.


@admin.register(BlogArticle)
class BlogArticleAdmin(admin.ModelAdmin):
    list_display = [
        "article_uuid", "article_title", "article_user", "category", "read_num", "privacy", "recommend",
        "update_time", "create_time", "is_delete"
    ]
    search_fields = ["article_uuid", "article_title", "article_user"]  # 搜索字段
    date_hierarchy = "create_time"  # 详细时间分层筛选　
    list_filter = ["article_title", "article_user", "category", "privacy", "is_delete"]  # 过滤器
    list_per_page = 50  # 设置每页显示多少条记录，默认是100条
    ordering = ("-create_time",)  # 设置默认排序字段，负号表示降序排序
    list_display_links = ("article_uuid", "article_title")  # 设置哪些字段可以点击进入编辑界面


@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = [
        "name", "category_type", "parents_catrgory", "update_time", "create_time", "is_delete"
    ]
    search_fields = ["name"]  # 搜索字段
    date_hierarchy = "create_time"  # 详细时间分层筛选　
    list_filter = ["name", "category_type", "parents_catrgory", "is_delete"]  # 过滤器
    list_per_page = 50  # 设置每页显示多少条记录，默认是100条
    ordering = ("-create_time",)  # 设置默认排序字段，负号表示降序排序


@xadmin.sites.register(BlogArticle)
class BlogUserXadmin():
    # 设置base_site.html的Title
    site_title = 'Blog运维资源管理系统'
    # 设置base_site.html的Footer
    site_footer = 'Blog运维资源管理系统'
    menu_style = "accordion"
    list_display = [
        "article_uuid", "article_title", "article_user", "category", "read_num", "privacy", "recommend",
        "update_time", "create_time", "is_delete"
    ]
    search_fields = ["article_uuid", "article_title", "article_user"]  # 搜索字段
    date_hierarchy = "create_time"  # 详细时间分层筛选　
    list_filter = ["article_title", "article_user", "category", "privacy", "is_delete"]  # 过滤器
    list_per_page = 50  # 设置每页显示多少条记录，默认是100条
    ordering = ("-create_time",)  # 设置默认排序字段，负号表示降序排序
    list_display_links = ("article_uuid", "article_title")  # 设置哪些字段可以点击进入编辑界面


@xadmin.sites.register(ArticleCategory)
class UserLoginIPXadmin():
    # 设置base_site.html的Title
    site_title = 'Blog运维资源管理系统'
    # 设置base_site.html的Footer
    site_footer = 'Blog运维资源管理系统'
    menu_style = "accordion"
    list_display = [
        "name", "category_type", "parents_catrgory", "update_time", "create_time", "is_delete"
    ]
    search_fields = ["name"]  # 搜索字段
    date_hierarchy = "create_time"  # 详细时间分层筛选　
    list_filter = ["name", "category_type", "parents_catrgory", "is_delete"]  # 过滤器
    list_per_page = 50  # 设置每页显示多少条记录，默认是100条
    ordering = ("-create_time",)  # 设置默认排序字段，负号表示降序排序