# Generated by Django 4.2.5 on 2023-11-17 14:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('term', '0014_alter_term_cdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='term',
            name='cdate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 17, 16, 24, 25, 848982)),
        ),
    ]
