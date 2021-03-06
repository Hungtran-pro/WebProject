# Generated by Django 3.2.7 on 2021-11-18 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatrooms', '0003_auto_20211119_0236'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('sex', models.CharField(choices=[('1', 'Male'), ('2', 'Female'), ('3', 'Other')], default='1', max_length=10)),
                ('dob', models.CharField(max_length=250)),
                ('relationship', models.CharField(max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver_messages', to='chatrooms.user'),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender_messages', to='chatrooms.user'),
        ),
    ]
