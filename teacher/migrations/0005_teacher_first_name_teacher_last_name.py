# Generated by Django 4.1.4 on 2023-01-01 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_remove_gradepost_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='first_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='last_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]