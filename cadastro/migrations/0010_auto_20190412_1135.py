# Generated by Django 2.1.7 on 2019-04-12 14:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0009_auto_20190412_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='data_criacao',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 12, 14, 35, 9, 422130, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='restaurante',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]
