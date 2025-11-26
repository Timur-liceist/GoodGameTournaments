from django.contrib import admin

from tournaments.models import (
    BattleModel,
    EventForTimeTable,
    RequestTeamForTournamentModel,
    TournamentModel,
    TournamentNewsModel,
)

admin.site.register(TournamentModel)
admin.site.register(EventForTimeTable)
admin.site.register(TournamentNewsModel)
admin.site.register(RequestTeamForTournamentModel)
admin.site.register(BattleModel)
