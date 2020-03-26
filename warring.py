"""
xadmin需要:
future, django-crispy-forms, django-formtools==2.1, django-import-export

xadmin/views/dashboard.py 修改
    #render() got an unexpected keyword argument 'renderer'
    #修改bug, 添加renderer
    #by prism 2018/10/4
    def render(self, name, value, attrs=None, renderer=None):

1.pip install six
2.进入python3.6/site-packages
3.将six.py 复制到 django/utils即可
*********************************
mysql:
site-packages/django/db/backends/mysql/base.py文件注释掉 base.py 中如下部分（35/36行）,内容如下
if version < (1, 3, 3):
     raise ImproperlyConfigured("mysqlclient 1.3.3 or newer is required; you have %s" % Database.__version__)

"""