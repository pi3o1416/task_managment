
from django.urls import path
from .views import *

app_name='task'
urlpatterns = [
    path('create-task/', CreateTask.as_view(), name='create_task'),
    path('create-task-list/', CreatedTaskList.as_view(), name='created_task_list'),
]
