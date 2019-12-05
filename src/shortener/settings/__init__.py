import os

ENVIRONMENT = os.getenv('YEKTANET_ENV', 'local')

if ENVIRONMENT == 'staging':
    from .staging import *
elif ENVIRONMENT == 'production':
    from .production import *
elif ENVIRONMENT == 'local':
    from .local import *
else:
    raise Exception('BAD CONFIG')
