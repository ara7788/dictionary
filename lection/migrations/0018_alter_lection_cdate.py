# Generated by Django 4.2.5 on 2023-11-17 20:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lection', '0017_lection_slug_alter_lection_cdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lection',
            name='cdate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 17, 22, 8, 41, 525293)),
        ),
    ]
