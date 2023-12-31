# Generated by Django 4.2.5 on 2023-11-05 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0003_alter_settings_start_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='telephone',
        ),
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.CharField(default='1@1.1', max_length=15, unique=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='maillog',
            name='status',
            field=models.CharField(choices=[('1', 'sent'), ('2', 'error')], default='1', max_length=1, verbose_name='статус'),
        ),
    ]
