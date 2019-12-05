import logging

from rest_framework.response import Response
from rest_framework.views import APIView

from shortener import errors
from .. import serializers
from ..services import signup as signup_services

logger = logging.getLogger(__name__)


class SignUpView(APIView):
    def post(self, request):
        data = serializers.SignUpSerializer(data=request.data)
        if data.is_valid():
            output = signup_services.create_client(username=data.validated_data['username'],
                                                   email=data.validated_data['email'],
                                                   password=data.validated_data['password'])

            return Response({
                'client': serializers.ClientSerializer(output['client']).data,
                'accessToken': output['tokens']['access_token'],
                'refreshToken': output['tokens']['refresh_token'],
            })
        else:
            logger.error(data.errors)
            raise errors.ShortenerError(errors.API_INVALID_REQUEST)
