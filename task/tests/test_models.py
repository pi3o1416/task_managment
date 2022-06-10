
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import TestCase
from django.utils import timezone
from task.models import Task, TaskAssignment, TaskSubmission

User = get_user_model()


class TestTask(TestCase):
    def setUp(self):
        self.group = Group.objects.create(
            name='general_user'
        )
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@gmail.com',
            password='1234',
        )
        self.task = Task.objects.create(
            headline='this is test task',
            created_by = self.user,
            last_date = timezone.now() + timezone.timedelta(days=4),
            description = 'test task description'
        )

    def test_headline_max_length(self):
        self.assertEqual(self.task._meta.get_field('headline').max_length, 200)

    def test_created_at_verbose_name(self):
        self.assertEqual(self.task._meta.get_field('created_at').verbose_name, 'Task creation time')

    def test_last_date_verbose_name(self):
        self.assertEqual(self.task._meta.get_field('last_date').verbose_name, 'Last date of submission')

    def test_description_verbose_name(self):
        self.assertEqual(self.task._meta.get_field('description').verbose_name, 'Task description')

    def test__str__(self):
        self.assertEqual(self.task.__str__(), self.task.headline)


class TestTaskAssignment(TestCase):
    def setUp(self):
        self.group = Group.objects.create(
            name='general_user'
        )
        self.user1 = User.objects.create_user(
            username='testuser1',
            email='testuser1@gmail.com',
            password='1234',
        )
        self.user2 = User.objects.create_user(
            username='testuser2',
            email='testuser2@gmail.com',
            password='1234',
        )
        self.task = Task.objects.create(
            headline='this is test task',
            created_by = self.user1,
            last_date = timezone.now() + timezone.timedelta(days=4),
            description = 'test task description'
        )
        self.taskassignment = TaskAssignment.objects.create(
            task = self.task,
            assigned_to = self.user2
        )

    def test_assigned_at_verbose_name(self):
        self.assertEqual(self.taskassignment._meta.get_field('assigned_at').verbose_name, 'Task assigned at')

    def test_assigned_at_auto_now_add(self):
        difference = timezone.now() - self.taskassignment.assigned_at
        self.assertLessEqual(difference , timezone.timedelta(minutes=1))

    def test_is_submitted_default(self):
        self.assertEqual(self.taskassignment.is_submitted, False)

    def test_notified_default(self):
        self.assertEqual(self.taskassignment.notified, False)

    def test_get_absolute_url(self):
        self.assertEqual(self.taskassignment.get_absolute_url(), '/task/assignment/{}/submit/'.format(self.taskassignment.id))


