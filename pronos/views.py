from rest_framework import generics
from rest_framework import viewsets
from django.db.models import (OuterRef, Subquery)

from worldcupprono.permissions import GlobalUserPermission

from .models import (Match, Prono)
from .permissions import PronoPermission
from .serializers import (MatchSerializer, PronoSerializer)


class PronoViewSet(viewsets.ModelViewSet):
    permission_classes = (GlobalUserPermission, PronoPermission)
    serializer_class = PronoSerializer

    def get_queryset(self):
        return Prono.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MatchListView(generics.ListAPIView):
    permission_classes = (GlobalUserPermission, )
    serializer_class = MatchSerializer
    queryset = Match.objects\
        .select_related('team_domicile', 'team_visitor')\
        .prefetch_related('pronos')\
        .order_by('date')

    def get_queryset(self, *args, **kwargs):
        qs = super(MatchListView, self).get_queryset(*args, **kwargs)

        prono = Prono.objects.filter(
            user=self.request.user, match=OuterRef('pk'))

        return qs.annotate(
            prono_id=Subquery(prono.values('id')[:1]),
            prono_domicile=Subquery(prono.values('score_domicile')[:1]),
            prono_visitor=Subquery(prono.values('score_visitor')[:1]))
