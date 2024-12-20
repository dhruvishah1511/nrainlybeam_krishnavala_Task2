# shadowapp/middleware.py
from django.http import HttpResponseServerError
import logging
from datetime import datetime
from .models import ErrorLog

logger = logging.getLogger(__name__)

class ErrorLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
        except Exception as e:
            error_message = str(e)
            error_type = type(e).__name__
            timestamp = datetime.now()
            
           
            ErrorLog.objects.create(
                message=error_message,
                error_type=error_type,
                timestamp=timestamp,
                status_code=500
            )
            
            logger.error(f"Error occurred: {error_message}")
            return HttpResponseServerError("An error occurred")
        return response
