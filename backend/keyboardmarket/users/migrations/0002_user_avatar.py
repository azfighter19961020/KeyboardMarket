# Generated by Django 3.1.5 on 2021-09-23 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='', upload_to='avatar/'),
            preserve_default=False,
        ),
    ]
