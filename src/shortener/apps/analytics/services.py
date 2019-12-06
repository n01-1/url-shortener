import logging
from datetime import datetime

from django.db.models import Q

from shortener import errors
from shortener.apps.client.models import Url
from .models import Viewer, Statistics

logger = logging.getLogger(__name__)


def create_viewer(short_url, uid, agent):
    try:
        url = Url.objects.get(short_url=short_url)
        viewer = Viewer(url=url, uid=uid, agent=agent)
        viewer.save()
        return viewer
    except Url.DoesNotExist:
        raise errors.ShortenerError(errors.URL_NOT_FOUND)


def get_total_viewers(from_time, to_time):
    return Viewer.objects.filter(time__range=(from_time, to_time)).count()


def get_total_mobile_viewers(from_time, to_time):
    return Viewer.objects.filter(time__range=(from_time, to_time)).filter(
        Q(agent__contains='Mobile') | Q(agent__contains='iPhone')).count()


def get_total_desktop_viewers(from_time, to_time):
    return Viewer.objects.filter(time__range=(from_time, to_time)).exclude(
        Q(agent__contains='Mobile') | Q(agent__contains='iPhone')).count()


def get_total_firefox_viewers(from_time, to_time):
    return Viewer.objects.filter(time__range=(from_time, to_time)).filter(agent__contains='Firefox').count()


def get_total_chrome_viewers(from_time, to_time):
    return Viewer.objects.filter(time__range=(from_time, to_time)).filter(agent__contains='Chrome').count()


def get_total_opera_viewers(from_time, to_time):
    return Viewer.objects.filter(time__range=(from_time, to_time)).filter(agent__contains='OPR').count()


def get_total_ie_viewers(from_time, to_time):
    return Viewer.objects.filter(time__range=(from_time, to_time)).filter(agent__contains='IE').count()


def get_total_viewers_by_uid(from_time, to_time):
    return Viewer.objects.filter(time__range=(from_time, to_time)).values('uid').distinct().count()


def get_total_mobile_viewers_by_uid(from_time, to_time):
    return Viewer.objects.filter(time__range=(from_time, to_time)).filter(
        Q(agent__contains='Mobile') | Q(agent__contains='iPhone')).values(
        'uid').distinct().count()


def get_total_desktop_viewers_by_uid(from_time, to_time):
    return Viewer.objects.filter(time__range=(from_time, to_time)).exclude(
        Q(agent__contains='Mobile') | Q(agent__contains='iPhone')).values(
        'uid').distinct().count()


def get_total_firefox_viewers_by_uid(from_time, to_time):
    return Viewer.objects.filter(time__range=(from_time, to_time)).filter(agent__contains='Firefox').values(
        'uid').distinct().count()


def get_total_chrome_viewers_by_uid(from_time, to_time):
    return Viewer.objects.filter(time__range=(from_time, to_time)).filter(agent__contains='Chrome').values(
        'uid').distinct().count()


def get_total_opera_viewers_by_uid(from_time, to_time):
    return Viewer.objects.filter(time__range=(from_time, to_time)).filter(agent__contains='OPR').values(
        'uid').distinct().count()


def get_total_ie_viewers_by_uid(from_time, to_time):
    return Viewer.objects.filter(time__range=(from_time, to_time)).filter(agent__contains='IE').values(
        'uid').distinct().count()


def execute_report_query(from_time, to_time, url_id):
    try:
        Url.objects.get(id=url_id)
    except Url.DoesNotExist:
        raise errors.ShortenerError(errors.URL_NOT_FOUND)

    return Statistics.objects.filter(time__range=(from_time.timestamp(), to_time.timestamp())).filter(url_id=url_id)


def get_today_report(url_id):
    today = datetime.today()
    from_time = datetime(year=today.year, month=today.month, day=today.day, hour=0, minute=0)
    to_time = datetime(year=today.year, month=today.month, day=today.day, hour=datetime.now().hour, minute=0)

    return execute_report_query(from_time, to_time, url_id)


def get_yesterday_report(url_id):
    today = datetime.today()
    from_time = datetime(year=today.year, month=today.month, day=today.day - 1, hour=0, minute=0)
    to_time = datetime(year=today.year, month=today.month, day=today.day, hour=0, minute=0)

    return execute_report_query(from_time, to_time, url_id)


def get_week_report(url_id):
    today = datetime.today()
    from_time = datetime(year=today.year, month=today.month, day=today.day - 7, hour=0, minute=0)
    to_time = datetime(year=today.year, month=today.month, day=today.day, hour=0, minute=0)

    return execute_report_query(from_time, to_time, url_id)


def get_month_report(url_id):
    today = datetime.today()
    from_time = datetime(year=today.year, month=today.month, day=today.day - 30, hour=0, minute=0)
    to_time = datetime(year=today.year, month=today.month, day=today.day, hour=0, minute=0)

    return execute_report_query(from_time, to_time, url_id)
