# Generated by Django 2.1.5 on 2019-02-12 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_map', '0002_auto_20190212_1508'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='map_data_base',
            new_name='MapDatabase',
        ),
    ]
