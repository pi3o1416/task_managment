
from django.urls import path
from .views import *


app_name = 'connection'
urlpatterns = [
    path('search/', SearchUser.as_view(), name='search_connection'),
    path('request-connection/', RequestConnection.as_view(), name='request_connection'),
    path('request-list', RequestList.as_view(), name='request_list'),
    path('confirm-connection/', ConfirmConnection.as_view(), name='confirm_connection'),
    path('', ConnectionList.as_view(), name='connection_list')
]
