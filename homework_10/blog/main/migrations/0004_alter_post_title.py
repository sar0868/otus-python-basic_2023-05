# Generated by Django 4.2.6 on 2023-10-09 12:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0003_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
