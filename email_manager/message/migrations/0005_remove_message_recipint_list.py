# Generated by Django 3.1.7 on 2021-03-16 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0004_auto_20210316_1136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='recipint_list',
        ),
    ]
