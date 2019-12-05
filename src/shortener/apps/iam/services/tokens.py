import time

import jwt
from django.conf import settings

from shortener import errors
from shortener.utils.password import compare_password
from ..models import User


def token_generator(user):
    expiration_time = round(time.time()) + settings.CONFIG['iam']['accessToken']['expiration']
    access_token = jwt.encode(
        payload={
            'sub': str(user.id),
            'exp': expiration_time,
        }, key=settings.CONFIG['iam']['accessToken']['key'], algorithm='HS256')

    refresh_expiration_time = round(time.time()) + settings.CONFIG['iam']['refreshToken']['expiration']
    refresh_token = jwt.encode(
        payload={
            'sub': str(user.id),
            'exp': refresh_expiration_time,
        }, key=settings.CONFIG['iam']['refreshToken']['key'], algorithm='HS256')

    return {
        'access_token': access_token,
        'refresh_token': refresh_token,
        'user': user
    }


def password_token_generator(username, email, password):
    try:
        if username is not None:
            user = User.objects.get(username=username)

            if not compare_password(password, user.password):
                raise errors.ShortenerError(errors.IAM_WRONG_PASSWORD)

            tokens = token_generator(user)
            return tokens

        if email is not None:
            user = User.objects.get(email=email)

            if not compare_password(password, user.password):
                raise errors.ShortenerError(errors.IAM_WRONG_PASSWORD)

            tokens = token_generator(user)
            return tokens

    except User.DoesNotExist:
        raise errors.ShortenerError(errors.IAM_USER_NOT_FOUND)


def refresh_token_generator(refresh_token):
    try:
        payload = jwt.decode(refresh_token, settings.CONFIG['iam']['refreshToken']['key'],
                             algorithms=['HS256'])
    except jwt.DecodeError:
        raise errors.ShortenerError(errors.IAM_REFRESH_TOKEN_INVALID)
    except jwt.ExpiredSignatureError:
        raise errors.ShortenerError(errors.IAM_REFRESH_TOKEN_EXPIRED)
    except jwt.InvalidTokenError:
        raise errors.ShortenerError(errors.IAM_REFRESH_TOKEN_INVALID)

    try:
        user = User.objects.get(id=payload['sub'])
    except User.DoesNotExist:
        raise errors.ShortenerError(errors.IAM_WRONG_CREDENTIALS)

    tokens = token_generator(user)
    return tokens


def get_user_info_from_access_token(token):
    try:
        payload = jwt.decode(token, settings.CONFIG['iam']['accessToken']['key'], algorithms=['HS256'])
    except jwt.DecodeError:
        raise errors.ShortenerError(errors.IAM_INVALID_ACCESS_TOKEN)
    except jwt.ExpiredSignatureError:
        raise errors.ShortenerError(errors.IAM_ACCESS_TOKEN_EXPIRED)
    except jwt.InvalidTokenError:
        raise errors.ShortenerError(errors.IAM_INVALID_ACCESS_TOKEN)

    return {'user_id': payload['sub']}
