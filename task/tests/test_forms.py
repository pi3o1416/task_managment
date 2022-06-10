
from django.test import TestCase
from django.utils import timezone

from task.forms import TaskForm
from task.models import Task

class TestTaskForm(TestCase):
    def setUp(self):
        self.data = {
            'description': 'this is form description',
            'last_date': timezone.now() + timezone.timedelta(days=3)
        }
        self.form = TaskForm(self.data)

    def test_last_date_label(self):
        self.assertEqual(self.form.fields['last_date'].label, 'Last date of submission')

    def test_description_label(self):
        self.assertEqual(self.form.fields['description'].label, 'Task description')



