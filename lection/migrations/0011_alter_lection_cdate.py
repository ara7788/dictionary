# Generated by Django 4.2.5 on 2023-11-09 13:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lection', '0010_alter_lection_cdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lection',
            name='cdate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 9, 15, 51, 53, 555115)),
        ),
    ]
