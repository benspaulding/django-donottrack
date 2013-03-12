# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.http import HttpRequest, HttpResponse
from django.test import TestCase

from ..context_processors import donottrack
from ..middleware import DoNotTrackMiddleware
from ..utils import get_donottrack


class GetDoNotTrackTestCase(TestCase):

    def setUp(self):
        self.request = HttpRequest()

    def test_http_dnt_header_not_present(self):
        self.assertFalse(get_donottrack(self.request))

    def test_http_dnt_header_is_1(self):
        self.request.META['HTTP_DNT'] = '1'
        self.assertTrue(get_donottrack(self.request))

    def test_http_dnt_header_is_not_1(self):
        self.request.META['HTTP_DNT'] = 1
        self.assertFalse(get_donottrack(self.request))

        self.request.META['HTTP_DNT'] = '0'
        self.assertFalse(get_donottrack(self.request))

        self.request.META['HTTP_DNT'] = 'wat'
        self.assertFalse(get_donottrack(self.request))


class DoNotTrackMiddlewareTestCase(TestCase):

    def test_process_request_sets_donottrack_attr(self):
        request = HttpRequest()
        result = DoNotTrackMiddleware().process_request(request)

        # Verify that ``None`` is returned, so Django will continue to process
        # the request.
        self.assertIsNone(result)

        # Now verify the side effect of the previous process_request call.
        self.assertTrue(hasattr(request, 'donottrack'))

    def test_process_response_adds_dnt_vary(self):
        response = DoNotTrackMiddleware().process_response(
                HttpRequest(), HttpResponse())
        # TODO: Use regex to be sure we match the right thing. This one fails
        # because we cannot check for start of string in the look-behind.
        # (look-behind requires fixed-width pattern.) Not sure how to get it
        # matching proplerly. ('DNT', 'WAT,DNT' 'DNT,WAT', 'WIDNT', 'DNTDOIT')
        # self.assertRegexpMatches(response['VARY'], r'(?<=^|,|\s)DNT(?=,|$)')
        self.assertIn('DNT', response['VARY'])


class DoNotTrackContextProcessorTestCase(TestCase):

    def test_donottrack_added_to_context(self):
        request = HttpRequest()
        DoNotTrackMiddleware().process_request(request)
        self.assertIn('donottrack', donottrack(request))

    def test_missing_middleware_raises_exception(self):
        with self.assertRaises(AttributeError):
            donottrack(HttpRequest())
