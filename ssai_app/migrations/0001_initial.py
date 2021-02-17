# Generated by Django 3.1.6 on 2021-02-17 10:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('mobile', models.IntegerField()),
                ('email', models.EmailField(max_length=256)),
                ('inquiry', models.CharField(max_length=50)),
                ('pay', models.CharField(max_length=100)),
                ('need', models.TextField()),
                ('date', models.DateField(default=datetime.datetime(2021, 2, 17, 10, 35, 35, 673224, tzinfo=utc))),
            ],
        ),
    ]
