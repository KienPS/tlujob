from rest_framework import serializers, generics
from job_recruitment.models import *
from accounts.models import User


class CurrentCandidateDefault:
    requires_context = True

    def __call__(self, serializer_field):
        candidate = generics.get_object_or_404(Candidate, user=serializer_field.context['request'].user)
        return candidate

    def __repr__(self):
        return '%s()' % self.__class__.__name__


class CurrentEmployerDefault:
    requires_context = True

    def __call__(self, serializer_field):
        employer = generics.get_object_or_404(Employer, user=serializer_field.context['request'].user)
        return employer

    def __repr__(self):
        return '%s()' % self.__class__.__name__


class ResumeSerializer(serializers.ModelSerializer):
    candidate = serializers.HiddenField(default=CurrentCandidateDefault())

    class Meta:
        model = Resume
        fields = '__all__'


class JobPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    employer = serializers.HiddenField(default=CurrentEmployerDefault())

    class Meta:
        model = Job
        fields = '__all__'


class ApplicationCandidateSerializer(serializers.ModelSerializer):
    candidate = serializers.HiddenField(default=CurrentCandidateDefault())

    class Meta:
        model = Application
        read_only_fields = ('status',)
        fields = '__all__'


class ApplicationEmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        read_only_fields = ('candidate', 'job',)
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'