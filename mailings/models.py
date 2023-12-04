from django.utils import timezone

from django.db import models


class Client(models.Model):
    """Получатели рассылки"""
    email = models.CharField(max_length=15, verbose_name='email', unique=True, default="1@1.1")
    FIO = models.TextField(max_length=100, verbose_name='Ф.И.О.')
    comment = models.TextField(blank = True, verbose_name='комментарий')

    def __str__(self):
        return self.FIO

class Message(models.Model):
    """Сообщение для рассылки"""
    title = models.CharField(max_length=150, verbose_name='Тема')
    body = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return self.title

class Settings(models.Model):
    """Настройки для рассылки - кому когда что отправлять"""
    class PeriodityType(models.TextChoices):
        ADAY = '1', 'ones a day'
        AWEEK = '2', 'ones a week'
        AMONTH = '3', 'ones a month'

    class StatusType(models.TextChoices):
        NEW = '1', 'new'
        ACTIVE = '2', 'active'
        FINISHED = '3', 'finished'

    start_date = models.DateTimeField(verbose_name='дата и время старта', default=timezone.now, null=True)
    period = models.CharField(max_length=1, choices=PeriodityType.choices, default=PeriodityType.AMONTH, verbose_name='периодичность')
    status = models.CharField(max_length=1, choices=StatusType.choices, default=StatusType.NEW, verbose_name='статус')
    client = models.ManyToManyField(Client)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)


class MailLog(models.Model):
    """История отправки рассылок"""
    class SendStatus(models.TextChoices):
        SENT = '1', 'sent'
        ERROR = '2', 'error'

    data_time = models.DateTimeField(verbose_name='дата и время отправки')
    status = models.CharField(max_length=1, choices=SendStatus.choices, default=SendStatus.SENT, verbose_name='статус')
    server_answer = models.TextField(verbose_name='ответ сервера', blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    settings = models.ForeignKey(Settings, on_delete=models.CASCADE, blank=True, null=True)

