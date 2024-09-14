from django.urls import path, include
from rest_framework import routers

from job_recruitment.views import *


app_name = 'job_recruitment'

router = routers.DefaultRouter()
router.register(r'resumes', ResumeViewSet, basename='resumes')
router.register(r'jobs', JobViewSet, basename='job_by_employer')
router.register(r'applications', ApplicationCandidateViewSet, basename='application_for_candidate')

urlpatterns = [
    path('public/jobs/', JobListAPIView.as_view()),
    path('public/jobs/<int:pk>', JobRetrieveAPIView.as_view()),
    path('jobs/<int:job_id>/applications/', ApplicationEmployerListAPIView.as_view()),
    path('jobs/<int:job_id>/applications/<int:pk>/', ApplicationEmployerRetrieveUpdateAPIView.as_view()),
    path('', include(router.urls)),
]