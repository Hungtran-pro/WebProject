# Generated by Django 3.2.7 on 2021-11-21 17:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatrooms', '0007_alter_message_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 22, 0, 47, 3, 155840)),
        ),
    ]