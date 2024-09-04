from typing import TYPE_CHECKING
import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

from job_recruitment.models import Company


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = models.CharField(max_length=11, blank=True)
    address = models.CharField(blank=True, max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True, related_name='members')
    is_manager = models.BooleanField(default=False)
