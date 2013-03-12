# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils.cache import patch_vary_headers

from .utils import get_donottrack


class DoNotTrackMiddleware(object):
    """
    Middleware that inspects the ``HTTP_DNT`` header and provides information
    for your app to act appropriately.

    """

    def process_request(self, request):
        """
        Inspects the request for the ``HTTP_DNT`` header and sets a
        ``donottrack`` attribute on the request object appropriately.

        Doing this here, rather than in a context processor, allows for your
        views to also take advantage of this logic.

        """
        request.donottrack = get_donottrack(request)

        return None

    def process_response(self, request, response):
        """
        Adds a vary header for ``DNT``, allowing for cache control based on the
        ``HTTP_DNT`` header.

        """
        patch_vary_headers(response, ('DNT',))

        return response
