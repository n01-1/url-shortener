from shortener.celery import app
from . import services
from .models import Statistics
import logging
from shortener.apps.client.models import Url
from datetime import datetime

logger = logging.getLogger(__name__)


@app.task()
def runner():
    urls = Url.objects.all()

    today = datetime.today()
    from_time = datetime(year=today.year, month=today.month, day=today.day, hour=datetime.now().hour - 1, minute=0)
    to_time = datetime(year=today.year, month=today.month, day=today.day, hour=datetime.now().hour, minute=0)

    for url in urls:
        try:
            statistics = Statistics(url=url)

            statistics.total_viewers = services.get_total_viewers(from_time.timestamp(), to_time.timestamp())
            statistics.total_mobile_viewers = services.get_total_mobile_viewers(from_time.timestamp(),
                                                                                to_time.timestamp())
            statistics.total_desktop_viewers = services.get_total_desktop_viewers(from_time.timestamp(),
                                                                                  to_time.timestamp())
            statistics.total_firefox_viewers = services.get_total_firefox_viewers(from_time.timestamp(),
                                                                                  to_time.timestamp())
            statistics.total_chrome_viewers = services.get_total_chrome_viewers(from_time.timestamp(),
                                                                                to_time.timestamp())
            statistics.total_opera_viewers = services.get_total_opera_viewers(from_time.timestamp(),
                                                                              to_time.timestamp())
            statistics.total_ie_viewers = services.get_total_ie_viewers(from_time.timestamp(), to_time.timestamp())

            statistics.total_viewers_by_uid = services.get_total_viewers_by_uid(from_time.timestamp(),
                                                                                to_time.timestamp())
            statistics.total_mobile_viewers_by_uid = services.get_total_mobile_viewers_by_uid(from_time.timestamp(),
                                                                                              to_time.timestamp())
            statistics.total_desktop_viewers_by_uid = services.get_total_desktop_viewers_by_uid(from_time.timestamp(),
                                                                                                to_time.timestamp())
            statistics.total_firefox_viewers_by_uid = services.get_total_firefox_viewers_by_uid(from_time.timestamp(),
                                                                                                to_time.timestamp())
            statistics.total_chrome_viewers_by_uid = services.get_total_chrome_viewers_by_uid(from_time.timestamp(),
                                                                                              to_time.timestamp())
            statistics.total_opera_viewers_by_uid = services.get_total_opera_viewers_by_uid(from_time.timestamp(),
                                                                                            to_time.timestamp())
            statistics.total_ie_viewers_by_uid = services.get_total_ie_viewers_by_uid(from_time.timestamp(),
                                                                                      to_time.timestamp())

            statistics.save()

        except Exception as e:
            logger.error(e)
