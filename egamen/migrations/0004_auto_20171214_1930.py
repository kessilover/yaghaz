# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-14 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egamen', '0003_story_lang'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='lang',
            field=models.BooleanField(default=True),
        ),
    ]
