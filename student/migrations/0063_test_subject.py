# Generated by Django 4.1.5 on 2023-02-03 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0022_remove_subject_detail_subject_grade'),
        ('student', '0062_remove_resulthistory_date_resulthistory_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='subject',
            field=models.ManyToManyField(to='teacher.subject'),
        ),
    ]