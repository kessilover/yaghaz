# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-14 20:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egamen', '0004_auto_20171214_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='has_chapter',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='story',
            name='lang',
            field=models.CharField(choices=[('LA', '-LANGUAGE-'), ('Ar', 'ARABIC'), ('Ot', 'OTHER')], default=('LA', '-LANGUAGE-'), max_length=3),
        ),
    ]
