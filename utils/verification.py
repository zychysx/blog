import re

from blog_user.models import BlogUser


def verification_username(request, data_dict):
    if not request.POST.get('username', None):
        return False
    if not 5 <= len(request.POST.get('username')) and len(request.POST.get('username')) >= 18:
        return False
    data_dict['username'] = request.POST.get('username')
    return data_dict


def verification_nick_name(request, data_dict):
    if not request.POST.get('nick_name', None):
        return False
    if not 5 <= len(request.POST.get('nick_name')) and len(request.POST.get('nick_name')) >= 10:
        return False
    data_dict['nick_name'] = request.POST.get('nick_name')
    return data_dict


def verification_username_exist(request):
    if not request.POST.get('username', None):
        return False
    if BlogUser.objects.filter(username=request.POST.get('username')).exists():
        return False
    return True

def verification_user_active(request):
    if not request.POST.get('username', None):
        return False
    obj = BlogUser.objects.get(username=request.POST.get('username', None))
    if not obj.is_active or obj.is_delete:
        return False
    return True


def verification_password(request, data_dict):
    if not request.POST.get('password', None):
        return False
    if not 8 <= len(request.POST.get('password')) and len(request.POST.get('password')) >= 20:
        return False
    data_dict['password'] = request.POST.get('password')
    return data_dict


def verification_ck_password(request):
    if not request.POST.get('ck_password', None):
        return False
    if not request.POST.get('password') == request.POST.get('ck_password'):
        return False
    return True


def verification_gender(request, data_dict):
    if not request.POST.get('gender', None):
        return False
    data_dict['gender'] = request.POST.get('gender')
    return data_dict


def verification_email(request, data_dict):
    if not request.POST.get('email', None):
        return False
    if not re.search(r'[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}', request.POST.get('email')):
        print(request.POST.get('email'))
        return False
    data_dict['email'] = request.POST.get('email')
    return data_dict


def verification_birthday(request, data_dict):
    if not request.POST.get('birthday', None):
        return False
    if not re.match(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$', request.POST.get('birthday')):
        return False
    data_dict['birthday'] = request.POST.get('birthday')
    return data_dict


def verification_sign_up(request):
    data_dict = {}
    if verification_nick_name(request, data_dict) and verification_username_exist(request) and verification_username(request, data_dict) and verification_password(request, data_dict) and verification_ck_password(request) and verification_gender(request, data_dict) and verification_email(request, data_dict) and verification_birthday(request, data_dict):
        return data_dict
    return False
