# Generated by Django 4.1.5 on 2023-06-20 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0004_staff_transfer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='modify_student',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='report_card',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='transfer',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='verify_user',
            field=models.BooleanField(default=True),
        ),
    ]
