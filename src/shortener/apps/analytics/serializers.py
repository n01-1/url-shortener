from rest_framework import serializers
import time


class StatisticsInputSerializer(serializers.Serializer):
    urlId = serializers.IntegerField(required=True, allow_null=False)


class StatisticsSerializer(serializers.BaseSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_representation(self, instance):
        return {
            'totalViewers': instance.total_viewers,
            'totalMobileViewers': instance.total_mobile_viewers,
            'totalDesktopViewers': instance.total_desktop_viewers,
            'totalFirefoxViewers': instance.total_firefox_viewers,
            'totalChromeViewers': instance.total_chrome_viewers,
            'totalOperaViewers': instance.total_opera_viewers,
            'totalIEViewers': instance.total_ie_viewers,
            'totalViewersByUid': instance.total_viewers_by_uid,
            'totalMobileViewersByUid': instance.total_mobile_viewers_by_uid,
            'totalDesktopViewersByUid': instance.total_desktop_viewers_by_uid,
            'totalFirefoxViewersByUid': instance.total_firefox_viewers_by_uid,
            'totalChromeViewersByUid': instance.total_chrome_viewers_by_uid,
            'totalOperaViewersByUid': instance.total_opera_viewers_by_uid,
            'totalIEViewersByUid': instance.total_ie_viewers_by_uid,
            'time': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(instance.time))
        }
