# Generated by Django 4.2.5 on 2023-11-09 13:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinehelper', '0010_alter_onlinehelper_cdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlinehelper',
            name='cdate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 9, 15, 51, 53, 553121)),
        ),
    ]
