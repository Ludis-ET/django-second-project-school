# Generated by Django 4.1.5 on 2023-02-18 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0035_rename_text_font_text_font_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='text',
            name='height',
        ),
        migrations.RemoveField(
            model_name='text',
            name='width',
        ),
    ]
