from rest_framework import generics, permissions

from accounts.models import User, Candidate, Employer
from accounts.serializers import UserSerializer, CandidateSerializer, EmployerSerializer, UserRegisterSerializer


class UserCreateAPIView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(serializer.validated_data['password'])
        instance.save()


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = ''
    lookup_url_kwarg = ''

    def get_object(self):
        return self.request.user


class CandidateCreateAPIView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CandidateSerializer
    queryset = Candidate.objects.all()


class CandidateRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CandidateSerializer
    queryset = Candidate.objects.all()
    lookup_field = ''
    lookup_url_kwarg = ''

    def get_object(self):
        return generics.get_object_or_404(Candidate, user=self.request.user)


class EmployerCreateAPIView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = EmployerSerializer
    queryset = Employer.objects.all()


class EmployerRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EmployerSerializer
    queryset = Employer.objects.all()
    lookup_field = ''
    lookup_url_kwarg = ''

    def get_object(self):
        return generics.get_object_or_404(Employer, user=self.request.user)
