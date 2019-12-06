import time

from django.db import models


class Viewer(models.Model):
    url = models.ForeignKey('shortener_client.Url', on_delete=models.CASCADE, blank=False)
    agent = models.CharField('Agent', max_length=60, blank=False)
    time = models.IntegerField('Time', default=time.time)
    uid = models.CharField('Cookie', max_length=256, blank=True)

    class Meta:
        verbose_name = 'Viewer'
        verbose_name_plural = 'Viewers'
        db_table = 'analytics_viewer'


class Statistics(models.Model):
    url = models.ForeignKey('shortener_client.Url', on_delete=models.CASCADE, blank=False, null=True)

    total_viewers = models.IntegerField(default=0)
    total_mobile_viewers = models.IntegerField(default=0)
    total_desktop_viewers = models.IntegerField(default=0)
    total_firefox_viewers = models.IntegerField(default=0)
    total_chrome_viewers = models.IntegerField(default=0)
    total_opera_viewers = models.IntegerField(default=0)
    total_ie_viewers = models.IntegerField(default=0)

    total_viewers_by_uid = models.IntegerField(default=0)
    total_mobile_viewers_by_uid = models.IntegerField(default=0)
    total_desktop_viewers_by_uid = models.IntegerField(default=0)
    total_firefox_viewers_by_uid = models.IntegerField(default=0)
    total_chrome_viewers_by_uid = models.IntegerField(default=0)
    total_opera_viewers_by_uid = models.IntegerField(default=0)
    total_ie_viewers_by_uid = models.IntegerField(default=0)

    time = models.IntegerField('Time', default=time.time)

    class Meta:
        verbose_name = 'Statistics'
        verbose_name_plural = 'Statistics'
        db_table = 'analytics_statistics'
