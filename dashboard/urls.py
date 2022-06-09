
from django.urls import path
from .views import Info, Dashboard

app_name = 'dashboard'
urlpatterns = [
    path('info/', Info.as_view(), name='info'),
    path('', Dashboard.as_view(), name='dashboard'),
]
