# Generated by Django 2.0 on 2018-02-01 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('egamen', '0026_auto_20180103_2027'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chapter',
            old_name='title',
            new_name='chapter_title',
        ),
    ]
