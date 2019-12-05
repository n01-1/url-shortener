from rest_framework import serializers
from django.conf import settings


class SignUpSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    email = serializers.EmailField(required=True, allow_null=False, allow_blank=False)
    password = serializers.CharField(required=True, min_length=5, allow_null=False, allow_blank=False)


class ClientSerializer(serializers.BaseSerializer):
    def __init__(self, *args, has_id=True, has_urls=False, **kwargs):
        self.has_id = has_id
        self.has_urls = has_urls

        super().__init__(*args, **kwargs)

    def to_representation(self, instance):
        val = {
            'username': instance.id.username,
            'email': instance.id.email,
        }

        if self.has_id:
            val['id'] = instance.id_id

        return val


class UrlInputSerializer(serializers.Serializer):
    longUrl = serializers.URLField(required=True, allow_null=False, allow_blank=False)
    recommendedUrl = serializers.CharField(required=False, allow_null=True, allow_blank=False)


class UrlSerializer(serializers.BaseSerializer):
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_representation(self, instance):
        val = {
            'longUrl': instance.long_url,
            'shortUrl': settings.CONFIG['shortener']['baseUrl'] + 'links/' + instance.short_url,
            'creationTime': instance.creation_time,
        }

        return val
