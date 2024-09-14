from rest_framework import serializers

from accounts.models import User, Candidate, Employer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'phone_number', 'address']
        # exclude = ['groups', 'user_permissions']
        # extra_kwargs = {
        #     'password': {
        #         'write_only': True,
        #     },
        # }


class CandidateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Candidate
        fields = '__all__'


class EmployerSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Employer
        fields = '__all__'
