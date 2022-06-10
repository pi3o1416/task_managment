
from django.shortcuts import render
from django.views import View
from .models import Notification

# Create your views here.


class NotificationList(View):
    template_name = 'notification/list_notifications.html'

    def get(self, request):
        notifications = self.get_queryset(request.user)
        print(notifications)
        return render(request, self.template_name, {'notifications': notifications})

    def get_queryset(self, user):
        notifications = Notification.objects.filter(notification_to=user)
        return notifications
