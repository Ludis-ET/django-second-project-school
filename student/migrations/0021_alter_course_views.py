# Generated by Django 4.1.4 on 2023-01-02 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0045_level_grade_alter_profile_grade_alter_profile_level'),
        ('student', '0020_course_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='views',
            field=models.ManyToManyField(blank=True, to='home.profile'),
        ),
    ]