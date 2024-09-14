import uuid

from django.db import models

from accounts.models import User, Candidate, Employer


class Resume(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='resumes/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Job(models.Model):
    JOB_TYPE_CHOICES = {
        'fulltime': 'Full-time',
        'parttime': 'Part-time',
        'contract': 'Contract',
    }

    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    address = models.TextField()
    type = models.CharField(max_length=16, choices=JOB_TYPE_CHOICES)
    salary_min = models.PositiveIntegerField(default=0)
    salary_max = models.PositiveIntegerField(default=0)
    requirements = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    date_expired = models.DateTimeField()
    last_updated = models.DateTimeField(auto_now=True)


class Application(models.Model):
    STATUS_CHOICES = {
        'pending': 'Pending',
        'accepted': 'Accepted',
        'rejected': 'Rejected',
    }

    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES)
    date_applied = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
