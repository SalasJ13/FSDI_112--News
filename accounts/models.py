from django.contrib.auth.models import AbstractUser
from django.db import models


class Role(models.Model):
    description = models.CharField(max_length=96)

    def __str__(self):
        return self.description


class Department(models.Model):
    description = models.CharField(max_length=96)

    def __str__(self):
        return self.description


class CustomUser(AbstractUser):
    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    years = models.PositiveIntegerField(
        null=True, blank=True
    )

#
# https://github.com/celiao/django-rest-authemail/issues/7
#
