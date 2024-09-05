from rest_framework import generics, permissions

from accounts.models import User
from accounts.serializers import UserSerializer, UserCompanySerializer
from accounts.permissions import *


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated & IsOwner]


class CompanyMemberPromotion(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCompanySerializer
    permission_classes = [permissions.IsAuthenticated & IsCompanyManager & IsSameCompany]


class CompanyAddMember(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCompanySerializer
    permission_classes = [permissions.IsAuthenticated & IsCompanyManager & ~IsObjInACompany]


class CompanyRemoveMember(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCompanySerializer
    permission_classes = [permissions.IsAuthenticated & IsCompanyManager & IsSameCompany]
