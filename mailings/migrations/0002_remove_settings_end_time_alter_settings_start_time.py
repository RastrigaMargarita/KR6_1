# Generated by Django 4.2.5 on 2023-10-01 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='end_time',
        ),
        migrations.AlterField(
            model_name='settings',
            name='start_time',
            field=models.TimeField(auto_now_add=True, verbose_name='время старта'),
        ),
    ]
