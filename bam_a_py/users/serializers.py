from .models import User, JobFunction
from rest_framework import serializers
from .fields import EnumField


class CoachSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'id', 'first_name', 'last_name')


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'job_function', 'last_name', 'coach', 'id')

    job_function = EnumField(enum=JobFunction)
    coach = CoachSerializer()
