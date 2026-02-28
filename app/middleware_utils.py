from .models import Visitor
from django.utils import timezone

def get_ip(request):
    """Get real client IP (supports proxy, Cloudflare, Nginx forward)."""
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        return x_forwarded_for.split(",")[0]
    return request.META.get("REMOTE_ADDR")


def track_visit(view_func):
    """Decorator used for each view."""
    def wrapper(request, *args, **kwargs):
        if request.user.is_staff:  # prevent admin visits
            return view_func(request, *args, **kwargs)

        ip = get_ip(request)
        user_agent = request.META.get("HTTP_USER_AGENT", "")

        # Check if the same IP visited the same page before
        visitor, created = Visitor.objects.get_or_create(
            ip_address=ip,
            path=request.path,
            defaults={"user_agent": user_agent}
        )

        if not created:
            visitor.visit_count += 1
            visitor.last_visit = timezone.now()
            visitor.save()

        return view_func(request, *args, **kwargs)

    return wrapper
