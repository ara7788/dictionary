# Generated by Django 4.2.5 on 2023-11-17 14:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('help', '0003_rename_ancore_help_anchor_alter_help_cdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='help',
            name='cdate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 17, 16, 19, 18, 99860)),
        ),
    ]
