# Generated by Django 3.1.7 on 2021-03-16 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0003_message_recipente_list'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='recipente_list',
            new_name='recipint_list',
        ),
    ]
