# Generated by Django 2.0 on 2018-01-01 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egamen', '0021_auto_20180101_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofiles',
            name='image',
            field=models.FileField(default='23.png', null=True, upload_to=''),
        ),
    ]