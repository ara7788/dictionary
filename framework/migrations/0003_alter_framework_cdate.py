# Generated by Django 4.2.3 on 2023-09-08 08:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('framework', '0002_alter_framework_cdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='framework',
            name='cdate',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 8, 11, 59, 30, 672040)),
        ),
    ]
