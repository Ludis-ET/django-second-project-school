# Generated by Django 4.1.5 on 2023-06-24 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0007_alter_staff_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='data',
            field=models.BooleanField(default=False),
        ),
    ]
