# Generated by Django 4.2.3 on 2023-09-08 08:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinehelper', '0002_rename_features_onlinehelper_stream_framework_features_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlinehelper',
            name='cdate',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 8, 11, 59, 30, 671043)),
        ),
    ]
