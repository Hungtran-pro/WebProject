# Generated by Django 3.2.7 on 2021-11-21 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20211119_0344'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
