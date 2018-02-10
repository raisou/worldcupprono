from django.contrib import admin

from .models import Invitation


@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    list_display = ('source', 'destination', 'email', 'board', 'created')
    search_fields = (
        'source__email',
        'source__username',
        'destination__email', 'destination__username', 'email', 'board__name')
    list_per_page = 20
