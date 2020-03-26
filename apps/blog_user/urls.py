from django.urls import path

from . import views


urlpatterns = [
    path(r'register.html', views.register, name='register.html'),
    path(r'register/', views.register, name='register'),
    path(r'login/', views.login, name='login'),
    path(r'logout/', views.logout, name='logout'),
]
