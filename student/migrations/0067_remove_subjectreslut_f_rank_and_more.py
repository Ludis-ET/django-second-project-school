# Generated by Django 4.1.5 on 2023-02-08 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0066_subjectreslut_f_rank_subjectreslut_rank_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjectreslut',
            name='f_rank',
        ),
        migrations.RemoveField(
            model_name='subjectreslut',
            name='rank',
        ),
        migrations.RemoveField(
            model_name='subjectreslut',
            name='s_rank',
        ),
        migrations.AddField(
            model_name='studentstatus',
            name='grade',
            field=models.IntegerField(null=True),
        ),
    ]
