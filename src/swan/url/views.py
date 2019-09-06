# from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
# import the logging library
import logging
from django.http import (
    HttpResponseRedirect,
    HttpResponse)
from django.views import View
from swan.url.models import URL


logger = logging.getLogger(__name__)


class URLView(View):
    def get(self, request, hash_id, *args, **kwargs):
        try:
            obj = URL.objects.get(hash_id=hash_id)
            return HttpResponseRedirect(obj.url)
        except Exception as e:
            logger.error(e)
            return HttpResponse(reason='Short URL not found.', status=404)
