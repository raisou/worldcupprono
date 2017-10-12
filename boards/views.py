from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from django.core.validators import validate_email, EMPTY_VALUES
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from worldcupprono.permissions import GlobalUserPermission

from .permissions import BoardPermission
from .serializers import BoardSerializer
from .models import Board


class BoardViewSet(viewsets.ModelViewSet):
    permission_classes = (GlobalUserPermission, BoardPermission)
    serializer_class = BoardSerializer
    queryset = Board.objects.all()

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

        for email in emails:
            try:
                if email in EMPTY_VALUES or not validate_email(email):
                    # TODO invitation with hash blabla xd
                    print('olol')
            except ValidationError as e:
                return Response(e, status=status.HTTP_400_BAD_REQUEST)
            finally:
                # well now we just add existing user for testing urpose
                for user_id in User.objects.filter(email__in=emails)\
                        .values_list('id', flat=True):
                    board.users.add(user_id)

        return Response(status=status.HTTP_200_OK)
