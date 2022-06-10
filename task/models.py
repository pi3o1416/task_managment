
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from .services import get_file_path

User = get_user_model()


class Task(models.Model):
    headline = models.CharField(max_length=200)
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='tasks')
    created_at = models.DateTimeField(
        _('Task creation time'),
        auto_now_add=True
    )
    last_date = models.DateTimeField(
        _('Last date of submission'),
    )
    description = models.TextField(_('Task description'))

    def __str__(self):
        return self.headline

    def get_absolute_url(self):
        pass


class TaskAssignment(models.Model):
    task = models.ForeignKey(to=Task, on_delete=models.CASCADE, related_name='assignments')
    assigned_to = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='assigned_tasks')
    assigned_at = models.DateTimeField(_('Task assigned at'), auto_now_add=True)
    is_submitted = models.BooleanField(default=False)
    notified = models.BooleanField(default=False)

    def __str__(self):
        return "{}-{}".format(self.task.headline, self.assigned_to.username)

    def get_absolute_url(self):
        return reverse('task:submit_task', kwargs={'id': self.pk})



class TaskSubmission(models.Model):
    assignment = models.ForeignKey(to=TaskAssignment, on_delete=models.CASCADE, related_name='submissions')
    submission_date = models.DateTimeField(_('Task submission date'), auto_now_add=True)
    attached_file = models.FileField(_('Attached files'), upload_to=get_file_path)




