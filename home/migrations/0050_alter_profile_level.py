# Generated by Django 4.1.5 on 2023-01-14 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0049_alter_profile_grade_alter_profile_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.level'),
        ),
    ]