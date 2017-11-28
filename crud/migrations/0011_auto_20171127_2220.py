# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-27 16:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0010_auto_20171104_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='ajax',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='ajax',
            name='number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='ajax',
            name='telephone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='ajax',
            name='updated_at',
            field=models.DateTimeField(),
        ),
    ]
