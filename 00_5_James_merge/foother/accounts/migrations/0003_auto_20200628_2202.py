# Generated by Django 2.1.15 on 2020-06-28 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200628_2154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_nick',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_score',
        ),
    ]
