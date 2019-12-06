from shortener import errors
from shortener.utils.redis import redis


def map_link(short_url):
    if redis.exists(short_url):
        url = redis.get(short_url)
        return url
    else:
        raise errors.ShortenerError(errors.URL_NOT_FOUND)
