# Generated by Django 3.2.3 on 2021-05-19 09:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customauth', '0023_alter_sessions_expiration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessions',
            name='expiration',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 19, 12, 21, 50, 289068)),
        ),
    ]