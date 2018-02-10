from rest_framework import serializers

from .models import (Match, Team, Prono)


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ('id', 'name', 'code')


class PronoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prono
        fields = ('id', 'score_domicile', 'score_visitor', 'match')
        read_only_fields = ('id', )


class MatchSerializer(serializers.ModelSerializer):
    team_domicile = TeamSerializer()
    team_visitor = TeamSerializer()
    prono_id = serializers.IntegerField(read_only=True)
    prono_domicile = serializers.IntegerField(read_only=True)
    prono_visitor = serializers.IntegerField(read_only=True)
    locked = serializers.BooleanField(source='is_locked', read_only=True)
    date = serializers.DateTimeField(format="%d/%m/%Y %H:%M")

    class Meta:
        model = Match
        fields = (
            'id',
            'prono_id',
            'prono_domicile',
            'prono_visitor',
            'team_domicile',
            'team_visitor',
            'score_domicile',
            'score_visitor', 'stage', 'date', 'locked', 'played')
