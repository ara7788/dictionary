# Generated by Django 4.2.5 on 2023-11-07 11:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_alter_article_cdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='cdate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 7, 13, 24, 16, 814681)),
        ),
    ]
