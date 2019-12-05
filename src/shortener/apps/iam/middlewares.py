import logging
import traceback

from django.http import JsonResponse

from shortener import errors
from .services.tokens import get_user_info_from_access_token

logger = logging.getLogger(__name__)


class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            if 'Authorization' in request.headers and request.headers['Authorization'] != 'notoken':
                if len(request.headers['Authorization']) < 8:
                    raise errors.ShortenerError(errors.IAM_INVALID_ACCESS_TOKEN)

                token = request.headers['Authorization'][7:]

                user_info = get_user_info_from_access_token(token)

                request.user_id = user_info['user_id']

                request.is_logged_in = True
            else:
                request.is_logged_in = False
        except Exception as ex:
            if type(ex) is errors.ShortenerError:
                return JsonResponse(data={
                    'error': {
                        'message': ex.info['error']['message'],
                        'userMessage': ex.info['error']['userMessage'],
                    }
                }, status=ex.info['status'])
            else:
                traceback.print_exc()
                return JsonResponse(data={
                    'error': {
                        'message': errors.SERVER_INTERNAL_ERROR['error']['message'],
                        'userMessage': errors.SERVER_INTERNAL_ERROR['error']['userMessage'],
                    }
                }, status=errors.SERVER_INTERNAL_ERROR['status'])

        response = self.get_response(request)
        return response
