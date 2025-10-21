from django.contrib import admin

from tournaments.models import (
    EventForTimeTable,
    RequestTeamForTournamentModel,
    TournamentModel,
    TournamentNews,
)

admin.site.register(TournamentModel)
admin.site.register(EventForTimeTable)
admin.site.register(TournamentNews)
admin.site.register(RequestTeamForTournamentModel)
