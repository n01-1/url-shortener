from shortener.utils.redis import redis


def map_link(short_url):
    url = redis.get(short_url)
    return url
