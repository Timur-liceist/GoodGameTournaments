from django.urls import path
from django.views.generic import TemplateView

from teams import views

app_name = "teams"

urlpatterns = [
    path(
        "select_type_team_view",
        TemplateView.as_view(
            template_name="teams/select_type_teams.html",
        ),
        name="select_type_team_view",
    ),
    path(
        "create",
        views.CreateTeamView.as_view(),
        name="create_team",
    ),
    path(
        "created_teams",
        views.TeamsCreatedByUserView.as_view(),
        name="created_teams_by_user",
    ),
    path(
        "member_teams",
        views.MemberTeamsView.as_view(),
        name="member_teams_by_user",
    ),
    path(
        "<int:team_id>/show_team",
        views.ShowTeamView.as_view(),
        name="show_team",
    ),
    path(
        "<int:invitation_id>/accept_invitation_team",
        views.AcceptInvitationTeamView.as_view(),
        name="accept_invitation_team",
    ),
    path(
        "<int:invitation_id>/reject_invitation_team",
        views.RejectInvitationTeamView.as_view(),
        name="reject_invitation_team",
    ),
    path(
        "my_invitations",
        views.MyInvitationsView.as_view(),
        name="my_invitations",
    ),
    path(
        "<int:team_id>/manage_team",
        views.ManageTeamView.as_view(),
        name="manage_team",
    ),
    path(
        "<int:team_id>/show_team",
        views.ManageTeamView.as_view(),
        name="show_team",
    ),
    path(
        "<int:team_id>/manage_team/invitations",
        views.ManageInvitations.as_view(),
        name="manage_invitations",
    ),
    path(
        "<int:team_id>/manage_team/<int:member_id>/change_role",
        views.ChangeRoleTeamView.as_view(),
        name="change_role_member_team",
    ),
    path(
        "<int:team_id>/manage_team/<int:member_id>/kick",
        views.KickMemberTeamView.as_view(),
        name="kick_member_team",
    ),
]
