import redis as redis_client
from django.conf import settings

redis = redis_client.Redis(host=settings.REDIS['HOST'],
                           port=settings.REDIS['PORT'],
                           password=settings.REDIS['PASSWORD'],
                           db=settings.REDIS['DB'])
