# Generated by Django 3.1.3 on 2021-05-12 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customauth', '0003_auto_20210513_0001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usr',
            name='id',
        ),
        migrations.AlterField(
            model_name='usr',
            name='username',
            field=models.CharField(default='', max_length=16, primary_key=True, serialize=False, unique=True),
        ),
    ]
