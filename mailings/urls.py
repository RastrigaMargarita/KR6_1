from django.contrib import admin
from django.urls import path, include
from django.views.decorators.cache import cache_page

from mailings.views import MailingListView, MailingCreateView, MessageCreateView, MailingUpdateView, MailingDeleteView, \
    LogListView

urlpatterns = [
    path('', MailingListView.as_view(template_name="mailings/mailing_list.html"), name='mailing_list'),
    path("mailing_create/", MailingCreateView.as_view(template_name = "mailings/mailing_create.html")),
    path("message_create/", MessageCreateView.as_view(template_name="mailings/message_create.html"), name='message_create'),
    path("mailing_update/<int:pk>/", cache_page(60)(MailingUpdateView.as_view(template_name = "mailings/mailing_create.html"))),
    path("mailing_delete/<int:pk>/", MailingDeleteView.as_view()),
    path("log_list/", LogListView.as_view(template_name = "mailings/log_list.html")),
]
