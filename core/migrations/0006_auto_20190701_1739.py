# Generated by Django 2.2.2 on 2019-07-01 21:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20190701_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_record',
            name='created_on',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
