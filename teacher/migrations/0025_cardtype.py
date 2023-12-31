# Generated by Django 4.1.5 on 2023-02-10 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0024_homeroom_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='cardType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.FloatField(blank=True)),
                ('height', models.FloatField(blank=True)),
                ('top', models.FloatField(blank=True)),
                ('bottom', models.FloatField(blank=True)),
                ('left', models.FloatField(blank=True)),
                ('right', models.FloatField(blank=True)),
                ('type', models.CharField(blank=True, max_length=255)),
                ('border', models.FloatField(blank=True)),
                ('borderColor', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
