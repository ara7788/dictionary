# Generated by Django 4.2.5 on 2023-11-17 14:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('framework', '0015_alter_framework_cdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='framework',
            name='cdate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 17, 16, 29, 17, 15351)),
        ),
    ]