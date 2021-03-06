# Generated by Django 3.0.3 on 2020-03-26 13:05

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogUser',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(db_column='is_del', default=False, verbose_name='是否删除')),
                ('user_uuid', models.UUIDField(default=uuid.uuid4, help_text='用户UUID', primary_key=True, serialize=False, verbose_name='UUID')),
                ('username', models.CharField(max_length=18, unique=True, verbose_name='用户名')),
                ('password', models.CharField(help_text='密码', max_length=128, verbose_name='密码')),
                ('nick_name', models.CharField(max_length=5, verbose_name='昵称')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='生日')),
                ('mobile', models.CharField(blank=True, max_length=14, null=True, verbose_name='手机号')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=8, verbose_name='性别')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='邮箱')),
                ('is_active', models.BooleanField(db_column='is_active', default=True, verbose_name='账号是否有效')),
                ('is_write', models.BooleanField(default=False, verbose_name='写作权限')),
                ('is_super', models.BooleanField(default=False, verbose_name='超级权限')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'user',
                'ordering': ('-create_time',),
            },
        ),
        migrations.CreateModel(
            name='UserLoginIP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(db_column='is_del', default=False, verbose_name='是否删除')),
                ('IP', models.GenericIPAddressField(verbose_name='IP地址')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='blog_user.BlogUser', verbose_name='用户')),
            ],
            options={
                'verbose_name': '登录IP',
                'verbose_name_plural': '登录IP',
                'db_table': 'user_ip',
                'ordering': ('-create_time',),
            },
        ),
    ]
