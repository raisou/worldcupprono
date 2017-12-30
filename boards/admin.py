from django.contrib import admin

from .models import Board


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'owner')
    search_fields = ('name', 'owner')
    list_per_page = 20
