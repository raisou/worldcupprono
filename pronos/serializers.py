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
    score_domicile = serializers.SerializerMethodField()
    score_visitor = serializers.SerializerMethodField()
    prono = serializers.SerializerMethodField()

    class Meta:
        model = Match
        fields = (
            'id',
            'prono',
            'team_domicile',
            'team_visitor',
            'stage', 'score_domicile', 'score_visitor', 'date')

    def get_prono(self, obj):
        user = self.context['request'].user
        if obj.pronos.filter(pronos__user=user).exists():
            return Prono.objects.get(
                user=user, match=obj.id).id
        return

    def get_score_domicile(self, obj):
        user = self.context['request'].user
        if obj.pronos.filter(pronos__user=user).exists():
            return Prono.objects.get(
                user=user, match=obj.id).score_domicile
        return obj.score_domicile

    def get_score_visitor(self, obj):
        user = self.context['request'].user
        if obj.pronos.filter(pronos__user=user).exists():
            return Prono.objects.get(
                user=user, match=obj.id).score_visitor
        return obj.score_visitor
