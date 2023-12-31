# Generated by Django 4.2.5 on 2023-09-28 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone', models.CharField(max_length=15, unique=True, verbose_name='телефон')),
                ('FIO', models.TextField(max_length=100, verbose_name='Ф.И.О.')),
                ('comment', models.TextField(blank=True, verbose_name='комментарий')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Тема')),
                ('body', models.TextField(verbose_name='Сообщение')),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(verbose_name='время старта')),
                ('end_time', models.TimeField(verbose_name='время старта')),
                ('period', models.CharField(choices=[('1', 'ones a day'), ('2', 'ones a week'), ('3', 'ones a month')], default='3', max_length=1, verbose_name='периодичность')),
                ('status', models.CharField(choices=[('1', 'new'), ('2', 'active'), ('3', 'finished')], default='1', max_length=1, verbose_name='статус')),
                ('client', models.ManyToManyField(to='mailings.client')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailings.message')),
            ],
        ),
        migrations.CreateModel(
            name='MailLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_time', models.DateTimeField(verbose_name='дата и время отправки')),
                ('status', models.CharField(choices=[('1', 'new'), ('2', 'sent'), ('3', 'error')], default='1', max_length=1, verbose_name='статус')),
                ('server_answer', models.TextField(blank=True, verbose_name='ответ сервера')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailings.client')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailings.message')),
            ],
        ),
    ]
