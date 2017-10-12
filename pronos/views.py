from rest_framework import generics
from rest_framework import viewsets

from worldcupprono.permissions import GlobalUserPermission

from .permissions import MatchPermission
from .permissions import TeamPermission
from .permissions import PronoPermission
from .serializers import MatchSerializer
from .serializers import TeamSerializer
from .serializers import PronoSerializer
from .serializers import StadeSerializer
from .models import Team
from .models import Match
from .models import Prono
from .models import Stade


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


class StadeListView(generics.ListAPIView):
    permission_classes = (GlobalUserPermission, )
    serializer_class = StadeSerializer
    queryset = Stade.objects.all()
