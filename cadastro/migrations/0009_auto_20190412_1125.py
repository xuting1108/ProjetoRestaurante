# Generated by Django 2.1.7 on 2019-04-12 14:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0008_auto_20190411_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='restaurante',
            field=models.CharField(default='Restaurante', max_length=200),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='data_criacao',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 12, 14, 25, 58, 727412, tzinfo=utc)),
        ),
    ]
