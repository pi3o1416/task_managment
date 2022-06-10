
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Task, TaskSubmission


class TaskForm(forms.ModelForm):
    last_date = forms.DateTimeField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label=_('Last date of submission'),
    )
    description = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'textarea'}),
        label=_('Task description')
    )

    class Meta:
        model = Task
        fields = ['headline', 'last_date', 'description']

    def save(self):
        task = super().save(commit=False)
        return task


class SubmissionForm(forms.ModelForm):
    class Meta:
        model = TaskSubmission
        fields = ['attached_file',]

