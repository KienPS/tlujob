from collections import UserList

from django.urls import path

from accounts.views import *


app_name = 'accounts'

urlpatterns = [
    path('companies/promote/<uuid:pk>/', CompanyMemberPromotion.as_view(), name='promote_user'),
    path('companies/add/<uuid:pk>/', CompanyAddMember.as_view(), name='add_user_to_company'),
    path('companies/remove/<uuid:pk>/', CompanyRemoveMember.as_view(), name='remove_user_from_company'),
    path('users/<uuid:pk>/', UserRetrieveUpdateDestroy.as_view(), name='user_retrieve_update_destroy'),
]