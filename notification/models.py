
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
User = get_user_model()


class Notification(models.Model):
    notification_headline=models.CharField(max_length=2000)
    notification_to=models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='notifications')
    description=models.TextField()
    notification_at=models.DateTimeField(_('Notification time'), auto_now_add=True)

    def __str__(self):
        return self.notification_headline




