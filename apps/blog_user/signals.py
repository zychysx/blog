from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password
from django.conf import settings

from blog_user.models import BlogUser


@receiver(post_save, sender=BlogUser)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """需要在app.py中设置"""
    if created:
        password = instance.password
        instance.password = make_password(password, None, settings.BLOG_ALG)
        instance.save()
