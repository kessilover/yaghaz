# Generated by Django 2.0 on 2018-01-01 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('egamen', '0023_auto_20180101_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofiles',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfiles',
        ),
    ]
