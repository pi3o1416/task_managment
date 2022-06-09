
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import TaskForm
from .models import Task

# Create your views here.


class CreateTask(LoginRequiredMixin, View):
    form_class = TaskForm
    template_name = 'task/create_task.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form = form.save()
            form.created_by = request.user
            form.save()
            return redirect(reverse('task:created_task_list'))
        return render(request, self.template_name, {'form': form})


class TaskDetail():
    pass


class EditTask():
    pass


class DeleteTask():
    pass


class TaskList():
    pass


class AssignTask():
    pass


class CreatedTaskList(LoginRequiredMixin, View):
    template_name = 'task/created_task_list.html'

    def get(self, request):
        tasks = self.get_queryset(request.user)
        return render(request, self.template_name, {'tasks': tasks})

    def get_queryset(self, user):
        tasks = Task.objects.filter(created_by=user).order_by('-created_at')
        return tasks
