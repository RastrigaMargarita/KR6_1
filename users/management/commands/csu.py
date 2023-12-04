import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
from django.core.management.base import BaseCommand
from users.models import User



class Command(BaseCommand):

    def handle(self, *args, **options):

        user = User.objects.create(
            email='rastrm@mail.ru',
            first_name='admin',
            last_name='admin',
            is_superuser=True,
            is_staff=True,
            is_active=True
        )
        user.set_password('123')
        user.save()
