from rest_framework import serializers

from .models import Match
from .models import Team
from .models import Prono
from .models import Stade


class StadeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stade
        fields = ('id', 'name', 'city')


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ('id', 'name', 'code')


class PronoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prono
        fields = (
            'id',
            'points', 'score_domicile', 'score_visitor', 'match', 'modified')
        read_only_fields = ('id', 'points', 'modified')


class MatchSerializer(serializers.ModelSerializer):
    team_domicile = TeamSerializer()
    team_visitor = TeamSerializer()
    location = StadeSerializer()
    score_domicile = serializers.SerializerMethodField()
    score_visitor = serializers.SerializerMethodField()
    pronos = PronoSerializer(source='users', many=True)

    class Meta:
        model = Match
        fields = (
            'id',
            'pronos',
            'team_domicile',
            'team_visitor',
            'description',
            'stage',
            'score_domicile', 'score_visitor', 'location', 'date')

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
