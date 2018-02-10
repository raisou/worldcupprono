from django.db.models import Q
from rest_framework import (mixins, viewsets, status)
from rest_framework.response import Response
from rest_framework.decorators import (list_route, detail_route)

from worldcupprono.permissions import GlobalUserPermission

from .models import Invitation
from .serializers import IvitationSerializer


class InvitationViewSet(
        mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (GlobalUserPermission, )
    serializer_class = IvitationSerializer

    def get_queryset(self):
        return Invitation.objects.filter(
            Q(status=Invitation.STATUS_PENDING),
            Q(source=self.request.user) | Q(destination=self.request.user))

    @detail_route(methods=['post'])
    def accept(self, request, pk=None):
        obj = self.get_queryset().get(pk=pk)
        obj.status = Invitation.STATUS_ACCEPTED
        obj.save()

        # add user to board
        obj.board.users.add(obj.destination)

        return Response(status=status.HTTP_200_OK)

    @list_route(methods=['post'])
    def accept_mail(self, request):
        token = self.request.data.get('token')
        if token:
            obj = self.get_queryset().get(token=token)
            if obj.destination and obj.destination != self.request.user:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            elif not obj.destination and self.request.user.email != obj.email:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                obj.status = Invitation.STATUS_ACCEPTED
                obj.save()

                # add user to board
                obj.board.users.add(self.request.user)

                return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    @detail_route(methods=['post'])
    def decline(self, request, pk=None):
        obj = self.get_queryset().get(pk=pk)
        obj.status = Invitation.STATUS_REFUSED
        obj.save()

        return Response(status=status.HTTP_200_OK)

    @detail_route(methods=['post'])
    def cancel(self, request, pk=None):
        obj = self.get_queryset().get(pk=pk)
        obj.status = Invitation.STATUS_CANCELED
        obj.save()

        return Response(status=status.HTTP_200_OK)

    @detail_route(methods=['post'])
    def resend(self, request, pk=None):
        obj = self.get_queryset().get(pk=pk)
        obj.send_invitation_mail()

        return Response(status=status.HTTP_200_OK)
