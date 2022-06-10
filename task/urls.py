
from django.urls import path
from .views import *

app_name='task'
urlpatterns = [
    path('create-task/', CreateTask.as_view(), name='create_task'),
    path('created-task-list/', CreatedTaskList.as_view(), name='created_task_list'),
    path('edit-task/<int:id>/', EditTask.as_view(), name='edit_task'),

]
