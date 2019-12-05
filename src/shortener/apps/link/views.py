from django.http import HttpResponseRedirect
from django.views import View

from . import services


class LinkView(View):
    def get(self, request, url):
        long_url = services.map_link(short_url=url)
        return HttpResponseRedirect(redirect_to=long_url)
