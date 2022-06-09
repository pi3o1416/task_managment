
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Task


class TaskForm(forms.ModelForm):
    last_date = forms.DateTimeField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label=_('Last Date of Submission'),
    )
    description = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'textarea'}),
        label=_('Description')
    )

    class Meta:
        model = Task
        fields = ['headline', 'last_date', 'description']

    def save(self):
        task = super().save(commit=False)
        return task
