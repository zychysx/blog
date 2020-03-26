from django.conf import settings


name_empty = {'status': 0, 'msg': 'username cannot be empty'}
name_exist = {'status': 0, 'msg': 'username does not exist'}
wrong_n_p = {'status': 0, 'msg': 'Wrong username or password'}

msg_frequency = '访问频率受限。未登录{}次/小时，登陆后{}/小时.'.format(settings.IP_FREQUENCY_NUM, settings.USER_FREQUENCY_NUM)
