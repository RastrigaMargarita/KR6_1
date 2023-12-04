from django.core.cache import cache

from config import settings
from mailings.models import Client


def get_all_clients():

    queryset = Client.objects.all()
    if settings.CACHE_ENABLED:
        key = 'all_clients'
        cache_data = cache.get(key)
        if cache_data is None:
            cache_data = queryset
            cache.set(key, cache_data)

        return cache_data

    return queryset

