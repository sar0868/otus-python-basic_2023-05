# Generated by Django 4.2.7 on 2023-11-06 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_user_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user_id',
            new_name='author_id',
        ),
    ]
