# coding: utf-8
from django.utils.deprecation import MiddlewareMixin
import logging

from TelephoneCard.settings import ignore_auth_urls

logger = logging.getLogger("django")


class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        url_path = request.path
        if url_path in ignore_auth_urls:
            return
