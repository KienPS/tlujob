from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.generics import get_object_or_404

from accounts.models import User, Candidate, Employer
from job_recruitment.models import Job


class IsJobCreator(BasePermission):
    def has_object_permission(self, request, view, obj):
        job_id = view.kwargs.get('job_id')
        job = get_object_or_404(Job, id=job_id)
        employer = get_object_or_404(Employer, user=request.user)
        return job.employer == employer