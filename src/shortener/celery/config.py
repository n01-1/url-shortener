from shortener import settings

broker_url = settings.RABBITMQ['URL']

task_serializer = 'json'

accept_content = ['json']

timezone = 'Asia/Tehran'

enable_utc = True
