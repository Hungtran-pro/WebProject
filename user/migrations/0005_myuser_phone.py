# Generated by Django 3.2.7 on 2021-11-21 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_myuser_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='phone',
            field=models.CharField(default='', max_length=11),
        ),
    ]
