# Generated by Django 4.1.5 on 2023-02-16 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0030_cardtable'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardtable',
            name='border',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cardtable',
            name='height',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cardtable',
            name='name_font',
            field=models.CharField(blank=True, max_length=2555, null=True),
        ),
        migrations.AddField(
            model_name='cardtable',
            name='name_size',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cardtable',
            name='num_font',
            field=models.CharField(blank=True, max_length=2555, null=True),
        ),
        migrations.AddField(
            model_name='cardtable',
            name='num_size',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cardtable',
            name='width',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cardtable',
            name='x_axis',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cardtable',
            name='y_axis',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cardtype',
            name='num',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cardtype',
            name='select',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='StudentName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('y_axis', models.FloatField(blank=True, null=True)),
                ('x_axis', models.FloatField(blank=True, null=True)),
                ('size', models.FloatField(blank=True, null=True)),
                ('font', models.CharField(blank=True, max_length=2555, null=True)),
                ('cardTable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.cardtype')),
            ],
        ),
        migrations.CreateModel(
            name='StudentGrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('y_axis', models.FloatField(blank=True, null=True)),
                ('x_axis', models.FloatField(blank=True, null=True)),
                ('size', models.FloatField(blank=True, null=True)),
                ('font', models.CharField(blank=True, max_length=2555, null=True)),
                ('cardTable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.cardtype')),
            ],
        ),
        migrations.CreateModel(
            name='icon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.FloatField(blank=True, null=True)),
                ('height', models.FloatField(blank=True, null=True)),
                ('y_axis', models.FloatField(blank=True, null=True)),
                ('x_axis', models.FloatField(blank=True, null=True)),
                ('border', models.FloatField(blank=True, null=True)),
                ('cardTable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.cardtype')),
            ],
        ),
    ]