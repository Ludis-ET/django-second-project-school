# Generated by Django 4.1.4 on 2023-01-05 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0035_resulthistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]