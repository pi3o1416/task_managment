
from django.contrib.auth import get_user_model

User = get_user_model()
MAX_NOTIFICATION_PER_PAGE = 10


def list_notifications(request):
    if request.user.is_authenticated:
        user = request.user
        notifications = user.notifications.all() \
            .order_by('notification_at')[:MAX_NOTIFICATION_PER_PAGE]
        return {'notifications': notifications}
    return {}
