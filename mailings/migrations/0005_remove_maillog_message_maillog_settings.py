# Generated by Django 4.2.5 on 2023-12-03 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0004_remove_client_telephone_client_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maillog',
            name='message',
        ),
        migrations.AddField(
            model_name='maillog',
            name='settings',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mailings.settings'),
        ),
    ]
