import logging

from rest_framework.response import Response
from rest_framework.views import APIView

from shortener import errors
from shortener.apps.iam import decorators
from .. import serializers
from ..services import client as client_services

logger = logging.getLogger(__name__)


class URLView(APIView):

    @decorators.require_login
    def post(self, request):
        data = serializers.UrlInputSerializer(data=request.data)
        if data.is_valid():
            url = client_services.create_link(user_id=request.user_id, long_url=data.validated_data['longUrl'],
                                              recommended_url=data.validated_data.get('recommendedUrl', None))

            return Response({
                'url': serializers.UrlSerializer(url).data
            })
        else:
            logger.error(data.errors)
            raise errors.ShortenerError(errors.API_INVALID_REQUEST)

    @decorators.require_login
    def get(self, request):
        urls = client_services.get_urls(request.user_id)
        return Response({
            'urls': serializers.UrlSerializer(urls, many=True).data
        })
