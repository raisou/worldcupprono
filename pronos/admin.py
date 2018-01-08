from django.contrib import admin

from .models import (Match, Team, Prono)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')
    list_per_page = 20


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = (
        '__str__', 'date', 'score_domicile', 'score_visitor', 'played')
    list_filter = ('stage', 'played')
    search_fields = ('team_domicile__name', 'team_visitor__name')
    list_per_page = 20


@admin.register(Prono)
class PronoAdmin(admin.ModelAdmin):
    list_display = ('match', 'user', 'score_domicile', 'score_visitor')
    search_fields = (
        'user__username',
        'match__team_domicile__name',
        'match__team_visitor__name')
    list_per_page = 20
