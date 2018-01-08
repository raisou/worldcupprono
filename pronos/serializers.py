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
    prono = serializers.SerializerMethodField()
    locked = serializers.BooleanField(source='is_locked', read_only=True)

    class Meta:
        model = Match
        fields = (
            'id',
            'prono',
            'team_domicile',
            'team_visitor', 'stage', 'date', 'locked', 'played')

    def get_prono(self, obj):
        try:
            return PronoSerializer(
                Prono.objects.get(
                    user=self.context['request'].user, match=obj.id)).data
        except Prono.DoesNotExist:
            return
