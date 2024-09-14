from collections import UserList

from django.urls import path

from accounts.views import *


app_name = 'accounts'

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('profile/', UserRetrieveUpdateDestroyView.as_view(), name='profile'),
    path('candidate/new/', CandidateCreateAPIView.as_view(), name='candidate_create'),
    path('candidate/', CandidateRetrieveUpdateAPIView.as_view(), name='candidate_retrieve_update'),
    path('employer/new/', EmployerCreateAPIView.as_view(), name='employer_create'),
    path('employer/', EmployerRetrieveUpdateAPIView.as_view(), name='employer_retrieve'),
]