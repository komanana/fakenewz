from django import http
from django.middleware.common import MiddlewareMixin
import traceback
from django.http import JsonResponse
import logging

logger = logging.getLogger(__name__)


class CorsMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if (request.method == "OPTIONS" and "HTTP_ACCESS_CONTROL_REQUEST_METHOD" in request.META):
            response = http.HttpResponse()
            response["Content-Length"] = "0"
            response["Access-Control-Max-Age"] = 86400
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "DELETE, GET, OPTIONS, PATCH, POST, PUT"
        response[
            "Access-Control-Allow-Headers"] = "accept, accept-encoding, authorization, content-type, dnt, origin, user-agent, x-csrftoken, x-requested-with"
        return response


class ExceptionMiddleware(MiddlewareMixin):
    """_summary_
       This is the Global Exception handler class, which can make all errors get managed.
    Args:
        MiddlewareMixin (_type_): _description_
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        traceback_info = traceback.format_exc()
        logger.info(f"request_path: {request.path}, traceback_info: {traceback_info}")
        return JsonResponse({"code": -1, "msg": "error"}, status=500)