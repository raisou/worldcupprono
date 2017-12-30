from django.contrib import admin

from .models import (Match, Team, Prono, Stade)


@admin.register(Stade)
class StadeAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
    search_fields = ('name', 'city')
    list_per_page = 20


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')
    list_per_page = 20


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = (
        '__str__', 'location', 'date', 'score_domicile', 'score_visitor')
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
