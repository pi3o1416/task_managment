
from django.db.models import Q
from django.utils import timezone
from notification.models import Notification
from .models import TaskAssignment


def push_notification():
    assignment_closeto_deadline = _get_assignment_close_to_deadline()
    print(assignment_closeto_deadline)
    for assignment in assignment_closeto_deadline:
        assignment_url = assignment.get_absolute_url()
        notification_headline = '<a href="{}">Assignment</a> {} is colse to deadline'.format(assignment_url, assignment.task)
        description = '<a href="{}">Assignment</a> is colse to deadline. \
                        Please Complete Your assignment withiin designeted time'.format(assignment_url)
        notification = Notification(
            notification_headline=notification_headline,
            notification_to=assignment.assigned_to,
            description=description,
        )
        notification.save()
        assignment.notified = True
        assignment.save()

def _get_assignment_close_to_deadline():
    today = timezone.now()
    tomorrow = today + timezone.timedelta(days=1)
    condition1 = Q(notified=False)
    condition2 = Q(task__last_date__lte=tomorrow)
    condition3 = Q(is_submitted=False)
    return TaskAssignment.objects.filter(condition1 & condition2 & condition3)
