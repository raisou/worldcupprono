from django.contrib import admin

from .models import Match
from .models import Team
from .models import Prono
from .models import Stade


class StadeAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
    search_fields = ('name', 'city')
    list_per_page = 20


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')
    list_per_page = 20


class MatchAdmin(admin.ModelAdmin):
    list_display = (
        '__str__', 'location', 'date', 'score_domicile', 'score_visitor')
    search_fields = ('team_domicile__name', 'team_visitor__name')
    list_per_page = 20


class PronoAdmin(admin.ModelAdmin):
    list_display = ('match', 'user', 'score_domicile', 'score_visitor')
    search_fields = (
        'user__username',
        'match__team_domicile__name',
        'match__team_visitor__name')
    list_per_page = 20

admin.site.register(Stade, StadeAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Prono, PronoAdmin)
