# Generated by Django 4.1.5 on 2023-08-04 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_remove_userlogin_active_login_userlogin_last_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userlogin',
            name='last_login',
        ),
        migrations.AddField(
            model_name='userlogin',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
