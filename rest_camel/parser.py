# -*- coding: utf-8 -*-
import json

from rest_framework.parsers import ParseError, six
from django.conf import settings

from rest_camel.settings import rest_framework_settings
from rest_camel.util import underscorize


class CamelCaseJSONParser(rest_framework_settings.PARSER_CLASS):
    def parse(self, stream, media_type=None, parser_context=None):
        parser_context = parser_context or {}
        encoding = parser_context.get('encoding', settings.DEFAULT_CHARSET)

        try:
            data = stream.read().decode(encoding)
            return underscorize(json.loads(data))
        except ValueError as exc:
            raise ParseError('JSON parse error - %s' % six.text_type(exc))
