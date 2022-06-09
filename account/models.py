
from django.contrib.auth.models import AbstractUser
from django.db import models
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


