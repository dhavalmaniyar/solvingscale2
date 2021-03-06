# Generated by Django 3.1.3 on 2021-02-20 11:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ssai_app', '0003_auto_20210220_1658'),
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('body', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 2, 20, 11, 39, 28, 645742, tzinfo=utc)),
        ),
    ]
