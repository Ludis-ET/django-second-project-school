# Generated by Django 4.1.5 on 2023-02-10 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0027_cardtype_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardtype',
            name='padding',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
