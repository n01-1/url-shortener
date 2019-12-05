import random
import string

from django.db import transaction

from shortener import errors
from shortener.utils.redis import redis
from ..models import Url, Client


def create_link(user_id, long_url, recommended_url):
    try:
        client = Client.objects.get(id_id=user_id)

        with transaction.atomic():
            url = Url(client=client, long_url=long_url)
            url.save()

            if recommended_url:
                try:
                    same_url = Url.objects.get(short_url=recommended_url)

                    if same_url:
                        short_url = recommended_url + ''.join(random.choices(string.digits + string.ascii_letters, k=2))
                        url.short_url = short_url
                        url.save()

                except Url.DoesNotExist:
                    url.short_url = recommended_url
                    url.save()

            else:
                short_url = ''.join(random.choices(string.digits + string.ascii_letters, k=10))
                url.short_url = short_url + str(user_id)
                url.save()

        redis.set(url.short_url, url.long_url)
        return url
    except Client.DoesNotExist:
        raise errors.ShortenerError(errors.CLIENT_NOT_FOUND)


def get_urls(user_id):
    return Url.objects.filter(client_id=user_id)
