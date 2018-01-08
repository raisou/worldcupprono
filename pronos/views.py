from rest_framework import generics
from rest_framework import viewsets

from worldcupprono.permissions import GlobalUserPermission

from .models import (Match, Prono)
from .permissions import (MatchPermission, PronoPermission)
from .serializers import (MatchSerializer, PronoSerializer)


class PronoViewSet(viewsets.ModelViewSet):
    permission_classes = (GlobalUserPermission, PronoPermission)
    serializer_class = PronoSerializer
    queryset = Prono.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MatchListView(generics.ListAPIView):
    permission_classes = (GlobalUserPermission, MatchPermission)
    serializer_class = MatchSerializer
    queryset = Match.objects\
        .select_related('team_domicile', 'team_visitor')\
        .prefetch_related('pronos')\
        .order_by('date')
