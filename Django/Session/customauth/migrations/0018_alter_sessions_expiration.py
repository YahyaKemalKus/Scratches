# Generated by Django 3.2.3 on 2021-05-13 21:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customauth', '0017_auto_20210513_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessions',
            name='expiration',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 14, 0, 18, 24, 115754)),
        ),
    ]
