
from django.urls import path
from .views import *

app_name='task'
urlpatterns = [
    path('create-task/', CreateTask.as_view(), name='create_task'),
    path('created-task-list/', CreatedTaskList.as_view(), name='created_task_list'),
    path('edit-task/<int:id>/', EditTask.as_view(), name='edit_task'),
    path('<int:id>/assign/', AssignTask.as_view(), name='assign_task'),
    path('task-queue/', TaskQueue.as_view(), name='task_queue'),
    path('assignment/<int:id>/submit/', SubmitTask.as_view(), name='submit_task'),
    path('delete-task/<int:id>/', DeleteTask.as_view(), name='delete_task'),

]
