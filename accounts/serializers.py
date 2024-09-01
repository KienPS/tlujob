from rest_framework import serializers

from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "phone_number"]


class UserCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["company", "is_manager"]
        read_only_fields = ["company"]
