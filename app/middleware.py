from django.test import TestCase

# Create your tests here.
from django.utils.deprecation import MiddlewareMixin
from .models import Visitor

class VisitorTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def process_request(self, request):
        if request.user.is_staff:
            return None

        ip = request.META.get("REMOTE_ADDR")
        user_agent = request.META.get("HTTP_USER_AGENT", "")

        Visitor.objects.create(
            ip_address=ip,
            path=request.path,
            user_agent=user_agent
        )

    def __call__(self, request):
        self.process_request(request)
        return self.get_response(request)
