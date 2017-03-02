# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 04:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('toys', '0004_auto_20170301_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='toy',
            name='zipcode',
            field=models.CharField(default=django.utils.timezone.now, max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(upload_to='photo'),
        ),
        migrations.AlterField(
            model_name='toy',
            name='age',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='toy',
            name='category',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='toy',
            name='condition',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='toy',
            name='msrp',
            field=models.CharField(max_length=45),
        ),
    ]