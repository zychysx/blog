# Generated by Django 3.0.3 on 2020-04-02 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='object_id',
            field=models.UUIDField(),
        ),
    ]
