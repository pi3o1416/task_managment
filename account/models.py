
from django.contrib.auth.models import Group
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(
        _('Email address'),
        unique=True
    )
    date_of_birth = models.DateField(
        _('Date of birth'),
        null=True
    )

    def __str__(self):
        return self.username

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)


@receiver(post_save, sender=User)
def add_to_general_gourp(sender, instance, **kwargs):
    group = Group.objects.get(name='general_user')
    group.user_set.add(instance)
