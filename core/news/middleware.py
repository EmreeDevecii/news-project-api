import logging

logger = logging.getLogger('news')

class LogRequestsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info(f"Yeni istek: {request.method} {request.get_full_path()} - Veri: {request.body}")
        response = self.get_response(request)
        logger.info(f"Istek sonuclandi: {response.status_code}")
        return response