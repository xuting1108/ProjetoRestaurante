# Generated by Django 2.1.7 on 2019-04-09 12:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_auto_20190409_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='data_criacao',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 9, 12, 58, 35, 399585, tzinfo=utc)),
        ),
    ]
