# Generated by Django 4.2.5 on 2023-12-03 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0006_remove_settings_start_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='дата и время старта'),
        ),
    ]