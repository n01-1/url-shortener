from django.db import transaction

from shortener import errors
from shortener.apps.iam.models import User
from shortener.apps.iam.services.tokens import token_generator
from shortener.utils.password import hash_password
from ..models import Client


def create_client(username, email, password):
    try:
        user = User.objects.get(username=username)

        if user:
            raise errors.ShortenerError(errors.IAM_USER_ALREADY_EXISTS)

    except User.DoesNotExist:
        with transaction.atomic():
            user = User(username=username, email=email)
            user.password = hash_password(password)
            user.save()

            client = Client(id=user)
            client.save()

            tokens = token_generator(user)

            return {
                'client': client,
                'tokens': tokens
            }
