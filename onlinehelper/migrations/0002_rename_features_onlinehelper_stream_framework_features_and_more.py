# Generated by Django 4.2.3 on 2023-09-08 07:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinehelper', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='onlinehelper',
            old_name='features',
            new_name='stream_framework_features',
        ),
        migrations.AddField(
            model_name='onlinehelper',
            name='stream_framework_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='onlinehelper',
            name='cdate',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 8, 10, 0, 54, 648631)),
        ),
    ]
