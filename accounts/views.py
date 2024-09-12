from rest_framework import generics, permissions, views, mixins

from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.urls import reverse

from django_rest_passwordreset.signals import reset_password_token_created
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.mixins import RetrieveModelMixin

from accounts.models import User
from accounts.serializers import UserSerializer, UserCompanySerializer, UserRegisterSerializer
from accounts.permissions import *


class UserCreateAPIView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(serializer.validated_data['password'])
        instance.save()


class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = ''
    lookup_url_kwarg = ''

    def get_object(self):
        return self.request.user

    # def get(self, request, *args, **kwargs):
    #     return self.get_object()


class UserProfileModify(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


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


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    # send an e-mail to the user
    context = {
        'current_user': reset_password_token.user,
        'username': reset_password_token.user.username,
        'email': reset_password_token.user.email,
        'reset_password_url': "{}?token={}".format(
            instance.request.build_absolute_uri(reverse('password_reset:reset-password-confirm')),
            reset_password_token.key)
    }

    # render email text
    email_html_message = render_to_string('email/user_reset_password.html', context)
    email_plaintext_message = render_to_string('email/user_reset_password.txt', context)

    msg = EmailMultiAlternatives(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )
    msg.attach_alternative(email_html_message, "text/html")
    msg.send()