# Generated by Django 3.1.5 on 2021-10-08 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default='<<email_address>>', max_length=255, verbose_name='電子郵箱'),
            preserve_default=False,
        ),
    ]