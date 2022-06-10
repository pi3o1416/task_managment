
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import TaskForm
from .models import Task, TaskAssignment

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


class EditTask(LoginRequiredMixin, UserPassesTestMixin, View):
    form_class = TaskForm
    template_name = 'task/edit_task.html'

    def get(self, request, id):
        task = self.get_object(id)
        form = self.form_class(instance=task)
        return render(request, self.template_name, {'form': form, 'task': task})

    def post(self, request, id):
        task = self.get_object(id)
        form = self.form_class(instance=task, data=request.POST)
        if form.is_valid():
            task = form.save()
            task.save()
            messages.success(request, 'Successfully Updated Profile')
        else:
            messages.error(request, 'Profile update request failed')
        return redirect(reverse('task:edit_task', args=[task.id]))

    def get_object(self, id):
        try:
            task = Task.objects.get(id=id)
            return task
        except Task.DoesNotExist:
            raise Http404

    def test_func(self):
        task = self.get_object(self.kwargs['id'])
        return task.created_by == self.request.user


class DeleteTask():
    pass


class TaskQueue(LoginRequiredMixin, View):
    template_name = 'task/task_queue.html'

    def get(self, request):
        assignments = self.get_queryset(request.user)
        return render(request, self.template_name, {'assignments': assignments})

    def get_queryset(self, user):
        return user.assigned_tasks.all().order_by('is_submitted').order_by('assigned_at')


class AssignTask(LoginRequiredMixin, UserPassesTestMixin, View):
    template_name = 'task/assign_task.html'

    def get(self, request, id):
        task = self.get_object(id)
        return render(request, self.template_name, {'task': task})

    def post(self, request, id):
        task = self.get_object(id)
        assign_to = request.POST.getlist('assign_to')
        for user in assign_to:
            task_assignment = TaskAssignment(task=task, assigned_to=user)
            task_assignment.save()
        return redirect(reverse('task:task_queue'))

    def get_object(self, id):
        try:
            task = Task.objects.get(id=id)
            return task
        except Task.DoesNotExist:
            raise Http404

    def test_func(self):
        task = self.get_object(self.kwargs['id'])
        return task.created_by == self.request.user


class CreatedTaskList(LoginRequiredMixin, View):
    template_name = 'task/created_task_list.html'

    def get(self, request):
        tasks = self.get_queryset(request.user)
        return render(request, self.template_name, {'tasks': tasks})

    def get_queryset(self, user):
        tasks = Task.objects.filter(created_by=user).order_by('-created_at')
        return tasks
