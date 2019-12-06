from django.contrib import admin

from .models import Viewer, Statistics


@admin.register(Viewer)
class ViewerAdmin(admin.ModelAdmin):
    list_display = ['uid', 'agent', ]


@admin.register(Statistics)
class StatisticsAdmin(admin.ModelAdmin):
    list_display = ['id', 'time', ]
