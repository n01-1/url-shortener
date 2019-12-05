import logging
import traceback

from django.utils.translation import gettext as _
from rest_framework import exceptions as rest_exceptions
from rest_framework import status
from rest_framework.response import Response

logger = logging.getLogger(__name__)


class ShortenerError(Exception):
    def __init__(self, info):
        self.info = info
        super().__init__(self.info['error']['message'])


SERVER_INTERNAL_ERROR = {
    'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
    'error': {
        'message': 'internal server error',
        'userMessage': _('خطای داخلی سرور'),
    }
}

API_INVALID_REQUEST = {
    'status': status.HTTP_400_BAD_REQUEST,
    'error': {
        'message': 'invalid request',
        'userMessage': _('ورودی اشتباه است'),
    }
}

SERVER_METHOD_NOT_ALLOWED = {
    'status': status.HTTP_405_METHOD_NOT_ALLOWED,
    'error': {
        'message': 'method not allowed',
        'userMessage': _('متد فراخوانده شده اشتباه است'),
    }
}

IAM_USER_NOT_FOUND = {
    'status': status.HTTP_404_NOT_FOUND,
    'error': {
        'message': 'client not found',
        'userMessage': _('کاربر یافت نشد'),
    }
}

IAM_USER_ALREADY_EXISTS = {
    'status': status.HTTP_409_CONFLICT,
    'error': {
        'message': 'user already exists',
        'userMessage': _('یوزر قبلا ثبت نام کرده است'),
    }
}

IAM_WRONG_CREDENTIALS = {
    'status': status.HTTP_400_BAD_REQUEST,
    'error': {
        'message': 'wrong credentials',
        'userMessage': _('اطلاعات ورود اشتباه است'),
    }
}

CLIENT_NOT_FOUND = {
    'status': status.HTTP_404_NOT_FOUND,
    'error': {
        'message': 'client not found',
        'userMessage': _('کاربر یافت نشد'),
    }
}

IAM_CLIENT_ALREADY_EXISTS = {
    'status': status.HTTP_409_CONFLICT,
    'error': {
        'message': 'client already exists',
        'userMessage': _('کاربر قبلا ثبت نام کرده است'),
    }
}

IAM_REFRESH_TOKEN_INVALID = {
    'status': status.HTTP_400_BAD_REQUEST,
    'error': {
        'message': 'refresh token is not valid',
        'userMessage': _('refresh token is not valid'),
    }
}

IAM_REFRESH_TOKEN_EXPIRED = {
    'status': status.HTTP_400_BAD_REQUEST,
    'error': {
        'message': 'refresh token is expired',
        'userMessage': _('دوباره وارد شوید (ورود شما منقضی شده است)'),
    }
}

IAM_INVALID_ACCESS_TOKEN = {
    'status': status.HTTP_401_UNAUTHORIZED,
    'error': {
        'message': 'access token is not valid',
        'userMessage': _('توکن ارسالی اشتباه است'),
    }
}

IAM_ACCESS_TOKEN_EXPIRED = {
    'status': status.HTTP_401_UNAUTHORIZED,
    'error': {
        'message': 'access token is expired',
        'userMessage': _('توکن ارسالی منقضی شده (لطفا دوباره وارد شوید)'),
    }
}

IAM_WRONG_PASSWORD = {
    'status': status.HTTP_400_BAD_REQUEST,
    'error': {
        'message': 'wrong password',
        'userMessage': _('رمز عبور اشتباه است'),
    }
}

IAM_LOGIN_REQUIRED = {
    'status': status.HTTP_401_UNAUTHORIZED,
    'error': {
        'message': 'login required',
        'userMessage': _('لطفا به سیستم وارد شوید'),
    }
}

URL_NOT_FOUND = {
    'status': status.HTTP_404_NOT_FOUND,
    'error': {
        'message': 'url not found',
        'userMessage': _('لینک مورد نظر یافت نشد'),
    }
}

def error_handler(ex, context):
    if type(ex) is ShortenerError:
        return Response({
            'error': {
                'message': ex.info['error']['message'],
                'userMessage': ex.info['error']['userMessage'],
            }
        }, status=ex.info['status'])
    elif type(ex) is rest_exceptions.MethodNotAllowed:
        return Response({
            'error': {
                'message': SERVER_METHOD_NOT_ALLOWED['error']['message'],
                'userMessage': SERVER_METHOD_NOT_ALLOWED['error']['userMessage'],
            }
        }, status=SERVER_METHOD_NOT_ALLOWED['status'])
    elif type(ex) is rest_exceptions.APIException:
        return Response({
            'error': {
                'message': ex.detail,
                'userMessage': ex.detail,
            }
        }, status=ex.status_code)
    else:
        traceback.print_exc()
        return Response({
            'error': {
                'message': SERVER_INTERNAL_ERROR['error']['message'],
                'userMessage': SERVER_INTERNAL_ERROR['error']['userMessage'],
            }
        }, status=SERVER_INTERNAL_ERROR['status'])
