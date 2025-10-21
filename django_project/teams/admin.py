from django.contrib import admin

from teams.models import InvitationToTeamModel, MemberModel, TeamModel

admin.site.register(TeamModel)
admin.site.register(MemberModel)
admin.site.register(InvitationToTeamModel)
