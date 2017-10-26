from rest_framework import serializers
from bam_a_py.contrib.fields import EnumField

from .models import Skill, Competency, SkillLevel


class SkillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'description', 'levels_examples', 'created_at', 'created_by', 'modified_at', 'url']

    created_by = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name="api:user-detail")
    url = serializers.HyperlinkedIdentityField(view_name="api:skill-detail")


class CompetencySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Competency
        fields = ['id', 'skill', 'user', 'level', 'created_at', 'url']

    level = EnumField(enum=SkillLevel)
    user = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name="api:user-detail")
    skill = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name="api:skill-detail")
    url = serializers.HyperlinkedIdentityField(view_name="api:competency-detail")


