# Generated by Django 4.1.4 on 2023-01-01 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_student_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='code',
            field=models.CharField(max_length=255, null=True),
        ),
    ]