# Generated by Django 2.0 on 2017-12-30 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egamen', '0013_auto_20171230_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='summary',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='story',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
