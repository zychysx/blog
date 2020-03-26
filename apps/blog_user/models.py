import uuid

from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator

from utils.models import BlogBaseModel

# Create your models here.


username_validator = UnicodeUsernameValidator()


class BlogUser(BlogBaseModel):
    """
    用户
    """
    user_uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, verbose_name="UUID",
                                 help_text="用户UUID")
    username = models.CharField(max_length=18, unique=True, verbose_name="用户名")
    password = models.CharField(max_length=128, verbose_name="密码", help_text="密码")
    nick_name = models.CharField(max_length=5, verbose_name="昵称")
    birthday = models.DateField(null=True, blank=True, verbose_name="生日")
    mobile = models.CharField(null=True, blank=True, max_length=14, verbose_name="手机号")
    gender = models.CharField(max_length=8, choices=(("male", u"男"), ("female", u"女")),
                              default="male", verbose_name="性别")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱")
    is_active = models.BooleanField(default=True, verbose_name="账号是否有效", db_column="is_active")
    is_write = models.BooleanField(default=False, verbose_name="写作权限")
    is_super = models.BooleanField(default=False, verbose_name="超级权限")

    class Meta:
        db_table = 'user'
        verbose_name = "用户"
        verbose_name_plural = "用户"
        ordering = ("-create_time", )

    def __str__(self):
        return self.username


class UserLoginIP(BlogBaseModel):
    IP = models.GenericIPAddressField(verbose_name="IP地址")
    user = models.ForeignKey(BlogUser, on_delete=models.DO_NOTHING,blank=True, null=True, verbose_name="用户")

    class Meta:
        db_table = 'user_ip'
        verbose_name = "登录IP"
        verbose_name_plural = "登录IP"
        ordering = ("-create_time", )

    def __str__(self):
        return self.IP
