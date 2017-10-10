from rest_framework.decorators import detail_route
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets

from .models import User
from .serializers import UserSerializer


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @detail_route()
    def coach(self, request, pk=None):
        user = self.get_object()
        coach = user.coach
        data = UserSerializer(instance=coach, context={'request': request}).data
        return Response(data)
