# Generated by Django 4.1.4 on 2022-12-25 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_rename_name_password_first_name_password_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='password',
            name='phone',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='password',
            name='sex',
            field=models.CharField(max_length=255, null=True),
        ),
    ]