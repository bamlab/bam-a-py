from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.postgres.fields import ArrayField
from enumfields import Enum, EnumField


class JobFunction(Enum):
    """Bamer's job function"""
    DEVELOPER = 'dev'
    BUSINESS_DEVELOPER = 'biz'
    UX_DESIGNER = 'ux'
    OPERATIONS = 'ops'


class User(AbstractUser):
    coach = models.ForeignKey("self", on_delete=models.SET_NULL, blank=True, null=True)
    job_function = EnumField(JobFunction, max_length=3, null=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
