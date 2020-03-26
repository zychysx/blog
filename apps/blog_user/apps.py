from django.apps import AppConfig


class BlogUserConfig(AppConfig):
    name = 'blog_user'
    verbose_name = "用户管理"

    def ready(self):
        import blog_user.signals
