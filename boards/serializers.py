from rest_framework import serializers

from clients.serializers import UserSerializer

from .models import Board


class BoardSerializer(serializers.ModelSerializer):
    is_owner = serializers.SerializerMethodField()
    users = UserSerializer(many=True, read_only=True)
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Board
        fields = ('id', 'name', 'owner', 'is_owner', 'users')

    def get_is_owner(self, obj):
        return self.context['request'].user == obj.owner
