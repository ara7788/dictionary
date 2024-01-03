# Generated by Django 4.2.5 on 2023-11-18 11:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('term', '0017_alter_term_cdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='term',
            name='slug',
            field=models.SlugField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='term',
            name='cdate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 18, 13, 15, 8, 191984)),
        ),
    ]
