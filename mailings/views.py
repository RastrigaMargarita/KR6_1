from datetime import datetime, timezone

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView

from mailings.forms import MailingForm
from mailings.management.commands.send_mails import Command
from mailings.models import Settings, Message, MailLog


class MailingCreateView(CreateView):
    model = Settings
    form_class = MailingForm

    success_url = reverse_lazy('mailing_list')

    def form_valid(self, form):
         if form.is_valid():
            new_mailing = form.save()
            new_mailing.save()
            if form.instance.start_date < datetime.now(tz=timezone.utc):
                if Command.check_active(form.instance):
                    Command.process_mailing(form.instance)
            return super().form_valid(form)

class MailingListView(ListView):
    model = Settings

    def get_clients(self, obj):
        return [client.FIO for client in obj.client.all()]


class MessageCreateView(CreateView):
    model = Message
    fields = ('title', 'body',)
    success_url = reverse_lazy('mailing_list')

class MailingUpdateView(UpdateView):
    model = Settings
    fields = ('start_date', 'period','status','client','message',)
    success_url = reverse_lazy('mailing_list')

class MailingDeleteView(DeleteView):
    model = Settings
    success_url = reverse_lazy('mailing_list')

class LogListView(ListView):
    model = MailLog
