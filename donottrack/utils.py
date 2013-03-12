# -*- coding: utf-8 -*-

from __future__ import unicode_literals


def get_donottrack(request):
    """
    Returns ``True`` if ``HTTP_DNT`` header is ``'1'``, ``False`` otherwise.

    """
    return request.META.get('HTTP_DNT') == '1'
