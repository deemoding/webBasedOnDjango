# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-22 07:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0005_auto_20160720_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]