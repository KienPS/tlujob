from enum import member

from rest_framework import generics, permissions, viewsets

from accounts.models import User
from job_recruitment.permissions import *
from job_recruitment.models import *
from job_recruitment.serializers import *


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [(IsOwner | ReadOnly) & permissions.IsAuthenticatedOrReadOnly]


# Through company pk
class CompanyMemberList(generics.ListAPIView):
    queryset = Company.objects.prefetch_related('members')
    serializer_class = CompanyMemberSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        self.queryset = self.queryset.filter(company_id=self.kwargs['company_id']).members.all()
        return self.queryset


class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [permissions.IsAuthenticated & IsOwner]

    def get_queryset(self):
        self.queryset = self.queryset.filter(user=self.request.user)
        return self.queryset


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [permissions.AllowAny]


class JobCategoryViewSet(viewsets.ModelViewSet):
    queryset = JobCategory.objects.all()
    serializer_class = JobCategorySerializer
    permission_classes = [permissions.AllowAny]


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly & IsInACompany]


class UserApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = UserApplicationSerializer
    permission_classes = [permissions.IsAuthenticated & IsOwner]

    def get_queryset(self):
        self.queryset = self.queryset.filter(user=self.request.user)
        return self.queryset


class JobApplicationList(generics.ListAPIView):
    queryset = Application.objects.all()
    serializer_class = JobReadOnlyApplicationSerializer
    permission_classes = [permissions.IsAuthenticated & IsCompanyOwner]

    def get_queryset(self):
        self.queryset = self.queryset.filter(job=self.kwargs['job_id'])
        return self.queryset


class JobApplicationRetrieve(generics.RetrieveAPIView):
    queryset = Application.objects.all()
    serializer_class = JobReadOnlyApplicationSerializer
    permission_classes = [permissions.IsAuthenticated & IsCompanyOwner]

    def get_queryset(self):
        self.queryset = self.queryset.filter(job=self.kwargs['job_id'])
        return self.queryset


class JobApplicationUpdate(generics.UpdateAPIView):
    queryset = Application.objects.all()
    serializer_class = JobUpdateApplicationSerializer
    permission_classes = [permissions.IsAuthenticated & IsCompanyOwner]

    def get_queryset(self):
        self.queryset = self.queryset.filter(job=self.kwargs['job_id'])
        return self.queryset
