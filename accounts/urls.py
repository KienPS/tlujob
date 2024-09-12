from collections import UserList

from django.urls import path

from accounts.views import *


app_name = 'accounts'

urlpatterns = [
    path('companies/promote/<uuid:pk>/', CompanyMemberPromotion.as_view(), name='promote_user'),
    path('companies/add/<uuid:pk>/', CompanyAddMember.as_view(), name='add_user_to_company'),
    path('companies/remove/<uuid:pk>/', CompanyRemoveMember.as_view(), name='remove_user_from_company'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('users/<uuid:pk>/', UserProfileModify.as_view(), name='user_retrieve_update_destroy'),
]