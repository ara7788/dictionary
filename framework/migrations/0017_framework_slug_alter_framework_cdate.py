# Generated by Django 4.2.5 on 2023-11-17 18:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('framework', '0016_alter_framework_cdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='framework',
            name='slug',
            field=models.SlugField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='framework',
            name='cdate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 17, 20, 44, 56, 875441)),
        ),
    ]
