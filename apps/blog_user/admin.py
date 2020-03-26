import xadmin

from xadmin import views
from django.contrib import admin

from .models import BlogUser, UserLoginIP

# Register your models here.


@admin.register(BlogUser)
class BlogUserAdmin(admin.ModelAdmin):
    list_display = ["user_uuid", "username", "nick_name", "gender", "email", "birthday", "is_write",
                    "is_active", "is_super", "update_time", "create_time", "is_delete"]  # 设置要显示在列表中的字段
    search_fields = ["user_uuid", "username", "nick_name", "email"]  # 搜索字段
    date_hierarchy = "create_time"  # 详细时间分层筛选　
    list_filter = ["gender", "is_write", "birthday", "is_delete"]  # 过滤器
    list_per_page = 50  # 设置每页显示多少条记录，默认是100条
    ordering = ("create_time",)  # 设置默认排序字段，负号表示降序排序
    list_display_links = ("user_uuid",) # 设置哪些字段可以点击进入编辑界面


@admin.register(UserLoginIP)
class UserLoginIPAdmin(admin.ModelAdmin):
    list_display = ["user", "IP", "update_time", "create_time", "is_delete"]
    search_fields = ["user", "IP"]
    date_hierarchy = "create_time"
    list_filter = ["user", "IP"]
    list_per_page = 50
    ordering = ("-create_time",)
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ("user", "IP")


admin.site.site_header = 'Blog运维资源管理系统'
admin.site.site_title = 'Blog运维'


"""xadmin配置"""


@xadmin.sites.register(views.CommAdminView)
class GlobalSetting(object):

    site_title = "Blog运维资源管理系统"  # 设置站点标题
    site_footer = "Blog运维资源管理系统"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠


@xadmin.sites.register(views.BaseAdminView)
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


@xadmin.sites.register(BlogUser)
class BlogUserXadmin():
    # 设置base_site.html的Title
    site_title = 'Blog运维资源管理系统'
    # 设置base_site.html的Footer
    site_footer = 'Blog运维资源管理系统'
    menu_style = "accordion"
    list_display = ["user_uuid", "username", "nick_name", "gender", "email", "birthday", "is_write",
                    "is_active", "is_super", "update_time", "create_time", "is_delete"]
    search_fields = ["user_uuid", "username", "nick_name", "email"]
    date_hierarchy = "create_time"
    list_filter = ["gender", "is_write", "birthday", "is_delete"]
    list_per_page = 50
    ordering = ("create_time",)
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ("user_uuid",)


@xadmin.sites.register(UserLoginIP)
class UserLoginIPXadmin():
    # 设置base_site.html的Title
    site_title = 'Blog运维资源管理系统'
    # 设置base_site.html的Footer
    site_footer = 'Blog运维资源管理系统'
    menu_style = "accordion"
    list_display = ["user", "IP", "update_time", "create_time", "is_delete"]
    search_fields = ["user", "IP"]
    date_hierarchy = "create_time"
    list_filter = ["user", "IP"]
    list_per_page = 50
    ordering = ("-create_time",)
    list_display_links =("user", "IP")

