# Generated by Django 4.1.5 on 2023-06-22 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redirector', '0011_subjectresluthistory_studentstatushistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='academicyear',
            name='new',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
