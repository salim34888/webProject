from django.utils import timezone
from django.shortcuts import redirect


class ProCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if hasattr(request, 'user') and request.user.is_authenticated:
            if request.user.pro_expiry and request.user.pro_expiry < timezone.now().date():
                request.user.pro_status = 'free'
                request.user.save()

        return self.get_response(request)