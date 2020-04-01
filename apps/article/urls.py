from django.urls import path

from . import views


urlpatterns = [
    path(r'write.html', views.write, name="write"),
    path(r'<uuid:article_uuid>.html', views.article_details, name='details'),
    path(r'list-<int:t>.html', views.article_list, name="blog_list_t"),
    path(r'list.html', views.article_list, name="blog_list"),
]
