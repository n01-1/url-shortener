import logging

from django.http import HttpResponseRedirect
from django.views import View

from shortener.utils.random import generator
from . import services
from . import tasks

logger = logging.getLogger(__name__)


class LinkView(View):
    def get(self, request, url):
        # TODO: save viewer in async way
        long_url = services.map_link(short_url=url)
        response = HttpResponseRedirect(redirect_to=long_url)

        try:
            uid = request.COOKIES['USER_IDENTIFIER']
            tasks.create_viewer.delay(url=url, uid=uid, agent=request.META['HTTP_USER_AGENT'])
            return response

        except KeyError:
            uid = generator(70)
            response.set_cookie('USER_IDENTIFIER', uid)
            tasks.create_viewer.delay(url=url, uid=uid, agent=request.META['HTTP_USER_AGENT'])
            return response
