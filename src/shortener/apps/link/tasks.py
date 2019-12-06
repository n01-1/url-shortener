from shortener.apps.analytics.services import create_viewer as create_viewer_service
from shortener.celery import app
import logging

logger = logging.getLogger(__name__)


@app.task()
def create_viewer(url, uid, agent):
    create_viewer_service(short_url=url, uid=uid, agent=agent)
