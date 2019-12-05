import logging
from functools import wraps

from shortener import errors

logger = logging.getLogger(__name__)


def require_login(fn):
    @wraps(fn)
    def wrapper_function(self, request, *args, **kwargs):
        if not request.is_logged_in:
            raise errors.ShortenerError(errors.IAM_LOGIN_REQUIRED)
        return fn(self, request, *args, **kwargs)

    return wrapper_function
