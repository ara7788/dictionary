# Generated by Django 4.2.5 on 2023-09-25 12:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('framework', '0004_alter_framework_cdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='framework',
            name='cdate',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 25, 15, 13, 3, 858579)),
        ),
    ]