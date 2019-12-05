from django.contrib import admin

from .models import Client, Url


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', ]


@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    list_display = ['short_url', 'long_url', ]
