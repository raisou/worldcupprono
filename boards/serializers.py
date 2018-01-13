from rest_framework import serializers
from django.contrib.auth.models import User
from djoser.serializers import UserSerializer

from .models import Board


class UserListSerializer(serializers.ModelSerializer):
    points = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            User._meta.pk.name,
            User.USERNAME_FIELD,
            'points'
        )
        read_only_fields = (User.USERNAME_FIELD,)

    def get_points(self, obj):
        score = 0
        for prono in obj.pronos.filter(match__played=True)\
                .select_related('match'):
            if prono.match.result == prono.result:
                if prono.match.score_domicile == prono.score_domicile and\
                        prono.match.score_visitor == prono.score_visitor:
                        score += 3
                else:
                    score += 1
        return score


class BoardListSerializer(serializers.ModelSerializer):
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Board
        fields = ('id', 'name', 'is_owner')

    def get_is_owner(self, obj):
        return self.context['request'].user == obj.owner


class BoardSerializer(serializers.ModelSerializer):
    is_owner = serializers.SerializerMethodField()
    users = UserListSerializer(many=True, read_only=True)
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Board
        fields = ('id', 'name', 'owner', 'is_owner', 'users')

    def get_is_owner(self, obj):
        return self.context['request'].user == obj.owner
