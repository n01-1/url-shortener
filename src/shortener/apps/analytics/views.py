import logging

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.response import Response
from rest_framework.views import APIView

from shortener import errors
from shortener.apps.iam.decorators import require_login
from . import services
from .serializers import StatisticsSerializer, StatisticsInputSerializer

logger = logging.getLogger(__name__)


class TodayStatisticsView(APIView):
    @require_login
    @method_decorator(cache_page(60))
    def get(self, request):
        data = StatisticsInputSerializer(data=request.query_params)
        if data.is_valid():
            statistics = services.get_today_report(data.validated_data['urlId'])
            logger.debug(statistics)
            return Response({
                'statistics': StatisticsSerializer(statistics, many=True).data
            })
        else:
            errors.ShortenerError(errors.API_INVALID_REQUEST)


class YesterdayStatisticsView(APIView):
    @require_login
    @method_decorator(cache_page(60))
    def get(self, request):
        data = StatisticsInputSerializer(data=request.query_params)
        if data.is_valid():
            statistics = services.get_yesterday_report(data.validated_data['urlId'])
            return Response({
                'statistics': StatisticsSerializer(statistics, many=True).data
            })
        else:
            errors.ShortenerError(errors.API_INVALID_REQUEST)


class WeekStatisticsView(APIView):
    @require_login
    @method_decorator(cache_page(60))
    def get(self, request):
        data = StatisticsInputSerializer(data=request.query_params)
        if data.is_valid():
            statistics = services.get_week_report(data.validated_data['urlId'])
            return Response({
                'statistics': StatisticsSerializer(statistics, many=True).data
            })
        else:
            errors.ShortenerError(errors.API_INVALID_REQUEST)


class MonthStatisticsView(APIView):
    @require_login
    @method_decorator(cache_page(60))
    def get(self, request):
        data = StatisticsInputSerializer(data=request.query_params)
        if data.is_valid():
            statistics = services.get_month_report(data.validated_data['urlId'])
            return Response({
                'statistics': StatisticsSerializer(statistics, many=True).data
            })
        else:
            errors.ShortenerError(errors.API_INVALID_REQUEST)
