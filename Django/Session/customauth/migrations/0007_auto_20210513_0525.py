# Generated by Django 3.1.3 on 2021-05-13 02:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customauth', '0006_auto_20210513_0524'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='sessions',
            table='AAsessions',
        ),
        migrations.AlterModelTable(
            name='usr',
            table='AAusers',
        ),
    ]
