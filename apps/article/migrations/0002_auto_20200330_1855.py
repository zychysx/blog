# Generated by Django 3.0.3 on 2020-03-30 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogarticle',
            name='article_title',
            field=models.CharField(max_length=100, unique=True, verbose_name='文章标题'),
        ),
    ]