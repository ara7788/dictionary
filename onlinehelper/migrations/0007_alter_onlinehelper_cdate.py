# Generated by Django 4.2.5 on 2023-11-02 14:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinehelper', '0006_alter_onlinehelper_cdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlinehelper',
            name='cdate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 2, 16, 52, 22, 711519)),
        ),
    ]
