import uuid

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from blog_user.models import BlogUser
from utils.models import BlogBaseModel

# Create your models here.


class ArticleCategory(BlogBaseModel):
    """文章类别"""
    CATEGORY_TYPE = (
        ("1", "一级类目"),
        ("2", "二级类目")
    )

    name = models.CharField(default="", max_length=50, verbose_name="类别名")
    category_type = models.CharField(default="", max_length=100, choices=CATEGORY_TYPE, )
    parents_catrgory = models.ForeignKey(
        "self", models.DO_NOTHING, null=True, blank=True, verbose_name="父类目级", related_name="sub_cat"
    )

    def tag_num(self):
        return BlogArticle.objects.filter(category=self.pk).count()

    class Meta:
        db_table = "article_category"
        verbose_name = "文章类别"
        verbose_name_plural = "文章类别"

    def __str__(self):
        return self.name


class BlogArticle(BlogBaseModel):
    """博客文章"""
    article_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name="UUID",
                                    help_text="文章UUID")
    article_title = models.CharField(max_length=100, unique=True, verbose_name="文章标题")
    article_user = models.ForeignKey(BlogUser, on_delete=models.DO_NOTHING, verbose_name="作者")
    category = models.ForeignKey(
        ArticleCategory, on_delete=models.DO_NOTHING, verbose_name="文章类别",
    )
    content = RichTextUploadingField(config_name='article_config')
    privacy = models.BooleanField(default=False, verbose_name="是否隐藏")
    read_num = models.IntegerField(default=0, verbose_name="阅读数")
    recommend = models.BooleanField(default=False, verbose_name="是否推荐")

    class Meta:
        db_table = "article"
        verbose_name = "文章"
        verbose_name_plural = "文章"
        ordering = ("-create_time", )

    def __str__(self):
        return self.article_title
