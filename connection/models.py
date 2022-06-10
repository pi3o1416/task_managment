
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Connection(models.Model):
    class StatusChoice(models.TextChoices):
        PENDING = 'PEN', _('Pending')
        ACCEPTED = 'ACC', _('Accepted')
        BLOCKED = 'BLC', _('Blocked')

    connected_to = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='connected_from'
    )
    connected_from = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='connected_to'
    )
    connected_at = models.DateTimeField(
        _('Connected Since'),
        auto_now_add=True
    )
    connection_status = models.CharField(
        max_length=3,
        choices=StatusChoice.choices,
        default=StatusChoice.PENDING
    )

    def __str__(self):
        return '{} -> {}'.format(self.connected_from, self.connected_to)





