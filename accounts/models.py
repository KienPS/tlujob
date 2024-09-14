from typing import TYPE_CHECKING
import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# from job_recruitment.models import Company


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    USER_ROLE = {
        'candidate': 'Ứng viên',
        'employer': 'Nhà tuyển dụng'
    }

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_("email address"), unique=True)
    phone_number = models.CharField(_("phone number"), max_length=11, blank=True)
    address = models.CharField(blank=True, max_length=255)
    # role = models.CharField(choices=USER_ROLE, max_length=32)


class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    skills = models.TextField(blank=True)
    experience_years = models.PositiveSmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(_("company name"), max_length=255)
    company_size = models.PositiveIntegerField(_("company size"), blank=True)
    industry = models.CharField(_("industry"), max_length=100)
    website = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)