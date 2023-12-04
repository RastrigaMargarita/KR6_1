from django.contrib import admin

from mailings.models import Client, Message, Settings, MailLog


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'FIO', 'comment')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body')

@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_date', 'period', 'status', 'message', 'get_clients')

    def get_clients(self, obj):
        return [client.FIO for client in obj.client.all()]

@admin.register(MailLog)
class MailLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'data_time', 'status', 'server_answer', 'client', 'settings')

