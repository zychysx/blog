from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from blog_user.models import BlogUser
from utils.models import BlogBaseModel

# Create your models here.


class Comment(BlogBaseModel):
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_uuid = models.UUIDField()
    content_object = GenericForeignKey('content_type', 'object_uuid')

    text = models.TextField()
    user = models.ForeignKey(BlogUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.user.nick_name

    class Meta:
        db_table = "comment"
        verbose_name = "评论"
        verbose_name_plural = "评论"
        ordering = ['-create_time']