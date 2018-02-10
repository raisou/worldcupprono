import logging

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from django.core.validators import validate_email, EMPTY_VALUES
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from invitations.models import Invitation
from worldcupprono.permissions import GlobalUserPermission

from .models import Board
from .permissions import (BoardPermission, BoardInvitePermission)
from .serializers import (BoardSerializer, BoardListSerializer)

logger = logging.getLogger(__name__)


class BoardViewSet(viewsets.ModelViewSet):
    permission_classes = (GlobalUserPermission, BoardPermission)
    serializer_class = BoardSerializer

    def get_serializer_class(self):
        if self.action in ['list']:
            return BoardListSerializer
        return self.serializer_class

    def get_queryset(self):
        return Board.objects.filter(users=self.request.user)

    def perform_create(self, serializer):
        board = serializer.save(owner=self.request.user)
        board.users.add(self.request.user)

    @detail_route(methods=['post'])
    def invite(self, request, pk=None):
        board = self.get_object()
        emails = request.data['emails']
        if emails in EMPTY_VALUES:
            return Response(
                'Veuillez entrer des emails à valider',
                status=status.HTTP_400_BAD_REQUEST)

        known_mails = User.objects.values_list('email', flat=True)

        for email in emails:
            if email in known_mails:
                Invitation.objects.create(
                    source=self.request.user,
                    destination=User.objects.get(email=email),
                    board=board,
                    status=Invitation.STATUS_PENDING)
            else:
                try:
                    validate_email(email)
                except ValidationError as e:
                    logger.warning(e)
                else:
                    Invitation.objects.create(
                        source=self.request.user,
                        email=email,
                        board=board,
                        status=Invitation.STATUS_PENDING)

        return Response(status=status.HTTP_200_OK)

    @detail_route(methods=['post'], permission_classes=[BoardInvitePermission])
    def leave(self, request, pk=None):
        board = self.get_object()
        board.users.remove(request.user)

        return Response(status=status.HTTP_200_OK)
