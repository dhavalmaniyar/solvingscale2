# Generated by Django 3.1.3 on 2021-02-20 11:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ssai_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 2, 20, 11, 28, 35, 82097, tzinfo=utc)),
        ),
    ]
