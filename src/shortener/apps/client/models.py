import time

from django.db import models


class Client(models.Model):
    id = models.OneToOneField('shortener_iam.User', on_delete=models.CASCADE, primary_key=True, related_name='client',
                              related_query_name='client')

    def __str__(self):
        return self.id.__str__()

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        db_table = 'client_client'


class Url(models.Model):
    client = models.ForeignKey('shortener_client.Client', on_delete=models.SET_NULL, blank=False, null=True)
    long_url = models.CharField('Long URL', max_length=512, blank=True)
    short_url = models.CharField('Short URL', max_length=256, blank=True, unique=True)
    creation_time = models.IntegerField('Creation Time', default=time.time)

    def __str__(self):
        return self.long_url

    class Meta:
        verbose_name = 'Url'
        verbose_name_plural = 'Urls'
        db_table = 'client_url'
