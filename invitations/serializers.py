from rest_framework import serializers

from boards.serializers import UserSerializer

from .models import Invitation


class IvitationSerializer(serializers.ModelSerializer):
    source = UserSerializer()
    destination = serializers.SerializerMethodField()
    board = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    is_source = serializers.SerializerMethodField()
    created = serializers.DateTimeField(format="%d/%m/%Y")

    class Meta:
        model = Invitation
        fields = (
            'id',
            'is_source', 'source', 'destination', 'board', 'status', 'created')
        read_only_fields = ('id', )

    def get_is_source(self, obj):
        return obj.source == self.context['request'].user

    def get_status(self, obj):
        return obj.get_status_display()

    def get_board(self, obj):
        return obj.board.name

    def get_destination(self, obj):
        return obj.destination.email if obj.destination else obj.email
