from enum import member

from rest_framework import generics, permissions, viewsets

from accounts.models import User, Candidate, Employer
# from job_recruitment.permissions import *
from job_recruitment.models import Resume, Job, Application, Notification
from job_recruitment.permissions import IsJobCreator
from job_recruitment.serializers import ResumeSerializer, JobSerializer, ApplicationCandidateSerializer, ApplicationEmployerSerializer, NotificationSerializer


class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        candidate = generics.get_object_or_404(Candidate, user=self.request.user)
        self.queryset = self.queryset.filter(candidate=candidate)
        return self.queryset


class JobListAPIView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]


class JobRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        employer = generics.get_object_or_404(Employer, user=self.request.user)
        self.queryset = self.queryset.filter(employer=employer)
        return self.queryset


class ApplicationCandidateViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationCandidateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        candidate = generics.get_object_or_404(Candidate, user=self.request.user)
        self.queryset = self.queryset.filter(candidate=candidate)
        return self.queryset


class ApplicationEmployerListAPIView(generics.ListAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationEmployerSerializer
    permission_classes = [permissions.IsAuthenticated & IsJobCreator]

    def get_queryset(self):
        employer = generics.get_object_or_404(Employer, user=self.request.user)
        job = generics.get_object_or_404(Job, id=self.kwargs['job_id'], employer=employer)
        self.queryset = self.queryset.filter(job=job)
        return self.queryset


class ApplicationEmployerRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationEmployerSerializer
    permission_classes = [permissions.IsAuthenticated & IsJobCreator]

    def get_queryset(self):
        employer = generics.get_object_or_404(Employer, user=self.request.user)
        job = generics.get_object_or_404(Job, id=self.kwargs['job_id'], employer=employer)
        self.queryset = self.queryset.filter(job=job)
        return self.queryset
