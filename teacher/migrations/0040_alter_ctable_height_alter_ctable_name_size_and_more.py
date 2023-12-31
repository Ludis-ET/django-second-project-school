# Generated by Django 4.1.5 on 2023-02-22 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0039_alter_ctable_border'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ctable',
            name='height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ctable',
            name='name_size',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ctable',
            name='num_size',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ctable',
            name='width',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ctable',
            name='x_axis',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ctable',
            name='y_axis',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='icon',
            name='border',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='icon',
            name='height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='icon',
            name='width',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='icon',
            name='x_axis',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='icon',
            name='y_axis',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='line',
            name='width',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='line',
            name='x_axis',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='line',
            name='y_axis',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentgrade',
            name='size',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentgrade',
            name='x_axis',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentgrade',
            name='y_axis',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentname',
            name='size',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentname',
            name='x_axis',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentname',
            name='y_axis',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='text',
            name='size',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='text',
            name='x_axis',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='text',
            name='y_axis',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
