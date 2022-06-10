
from django.urls import path
from .views import NotificationList


app_name='notification'
urlpatterns = [
    path('list/', NotificationList.as_view(), name='notification_list'),
]

