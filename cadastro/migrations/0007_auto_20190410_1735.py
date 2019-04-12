# Generated by Django 2.1.7 on 2019-04-10 20:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0006_auto_20190410_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos_restaurantes'),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='data_criacao',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 10, 20, 35, 54, 60914, tzinfo=utc)),
        ),
    ]
