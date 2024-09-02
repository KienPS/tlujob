from typing import TYPE_CHECKING
import uuid

from django.db import models

from django.conf import settings


class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Resume(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    attachment = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=100)


class JobCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Job(models.Model):
    WORKING_FORM_CHOICES = {
        'part-time': 'Part time',
        'full-time': 'Full time',
        'contract': 'Contract',
    }

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(JobCategory, on_delete=models.CASCADE, related_name='jobs')
    skills = models.ManyToManyField(Skill)
    salary_min = models.PositiveIntegerField()
    salary_max = models.PositiveIntegerField()
    working_form = models.CharField(max_length=16, choices=WORKING_FORM_CHOICES)
    min_year_of_exp = models.PositiveIntegerField(default=0)
    posted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expired_at = models.DateTimeField()
    resumes = models.ManyToManyField(Resume, through='Application')

    def __str__(self):
        return self.title


class Application(models.Model):
    STATUS_CHOICES = {
        'pending': 'Pending',
        'accepted': 'Accepted',
        'rejected': 'Rejected',
    }

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default='pending')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.resume.user.username} - {self.job.title}'
