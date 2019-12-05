from rest_framework import serializers


class GenerateTokenInputSerializer(serializers.Serializer):
    username = serializers.CharField(required=False, allow_blank=False, allow_null=True)
    email = serializers.CharField(required=False, allow_blank=False, allow_null=True)
    password = serializers.CharField(required=False, allow_blank=False, allow_null=True)
    grantType = serializers.CharField(required=True, allow_blank=False, allow_null=False)
    refreshToken = serializers.CharField(required=False, allow_blank=False, allow_null=True)


class UserSerializer(serializers.BaseSerializer):
    def __init__(self, *args, has_id=True, **kwargs):
        self.has_id = has_id
        super().__init__(*args, **kwargs)

    def to_representation(self, instance):
        val = {
            'username': instance.username,
            'email': instance.email,
        }

        if self.has_id:
            val['id'] = instance.id

        return val
