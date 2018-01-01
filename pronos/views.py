from rest_framework import generics
from rest_framework import viewsets

from worldcupprono.permissions import GlobalUserPermission

from .models import (Team, Match, Prono)
from .permissions import (MatchPermission, TeamPermission, PronoPermission)
from .serializers import (MatchSerializer, TeamSerializer, PronoSerializer)


class PronoViewSet(viewsets.ModelViewSet):
    permission_classes = (GlobalUserPermission, PronoPermission)
    serializer_class = PronoSerializer
    queryset = Prono.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TeamListView(generics.ListAPIView):
    permission_classes = (GlobalUserPermission, TeamPermission)
    serializer_class = TeamSerializer
    queryset = Team.objects.all()


class MatchListView(generics.ListAPIView):
    permission_classes = (GlobalUserPermission, MatchPermission)
    serializer_class = MatchSerializer
    queryset = Match.objects.order_by('date')
