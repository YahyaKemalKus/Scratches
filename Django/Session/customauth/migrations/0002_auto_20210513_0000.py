# Generated by Django 3.1.3 on 2021-05-12 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customauth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usr',
            name='password',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='usr',
            name='username',
            field=models.CharField(max_length=16, null=True, unique=True),
        ),
    ]
