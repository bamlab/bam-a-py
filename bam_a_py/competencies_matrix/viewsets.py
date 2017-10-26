from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Skill, Competency
from .serializers import SkillSerializer, CompetencySerializer


# ViewSets define the view behavior.
class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


# ViewSets define the view behavior.
class CompetencyViewSet(viewsets.ModelViewSet):
    queryset = Competency.objects.all()
    serializer_class = CompetencySerializer
