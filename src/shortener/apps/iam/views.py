import logging

from rest_framework.response import Response
from rest_framework.views import APIView

from shortener import errors
from . import serializers
from .services import tokens as tokens_services

logger = logging.getLogger(__name__)


class TokenView(APIView):
    def post(self, request):
        data = serializers.GenerateTokenInputSerializer(data=request.data)
        if data.is_valid():
            if data.validated_data['grantType'] == 'password':
                tokens = tokens_services.password_token_generator(username=data.validated_data.get('username', None),
                                                                  email=data.validated_data.get('email', None),
                                                                  password=data.validated_data['password'])

                return Response({
                    'accessToken': tokens['access_token'],
                    'refreshToken': tokens['refresh_token']
                })

            if data.validated_data['grantType'] == 'refreshToken':
                tokens = tokens_services.refresh_token_generator(refresh_token=data.validated_data['refreshToken'])

                return Response({
                    'accessToken': tokens['access_token'],
                    'refreshToken': tokens['refresh_token']
                })

        else:
            logger.error(data.errors)
            raise errors.ShortenerError(errors.API_INVALID_REQUEST)
