from rest_framework import serializers

from bam_a_py.contrib.fields import EnumField
from .models import User, JobFunction


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'job_function', 'last_name', 'coach', 'url')

    job_function = EnumField(enum=JobFunction)
    coach = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name="api:user-detail")
    url = serializers.HyperlinkedIdentityField(view_name="api:user-detail")
