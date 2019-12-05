from django.apps import AppConfig


class ClientConfig(AppConfig):
    name = 'shortener.apps.client'
    label = 'shortener_client'
    verbose_name = 'Client Management'
