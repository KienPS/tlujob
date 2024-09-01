from django.urls import path, include
from rest_framework import routers

from job_recruitment.views import *


app_name = 'job_recruitment'

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'resumes', ResumeViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'job_categories', JobCategoryViewSet)
router.register(r'jobs', JobViewSet)
router.register(r'applications', UserApplicationViewSet)

urlpatterns = [
    path('companies/<int:company_id>/members/', CompanyMemberList.as_view()),
    path('jobs/<int:job_id>/applications/', JobApplicationList.as_view()),
    path('jobs/<int:job_id>/applications/<uuid:pk>/', JobApplicationRetrieve.as_view()),
    path('jobs/<int:job_id>/applications/<uuid:pk>/update/', JobApplicationUpdate.as_view()),
    path('', include(router.urls)),
]