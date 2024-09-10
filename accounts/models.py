from typing import TYPE_CHECKING
import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from job_recruitment.models import Company


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_("email address"), unique=True)
    phone_number = models.CharField(_("phone number"), max_length=11, blank=True)
    address = models.CharField(blank=True, max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True, related_name='members')
    is_manager = models.BooleanField(_("is company's manager"), default=False)
