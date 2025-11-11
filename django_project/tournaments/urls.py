from django.urls import path
from django.views.generic import TemplateView

from tournaments import views

app_name = "tournaments"

urlpatterns = [
    path(
        "create",
        views.TournamentCreateView.as_view(),
        name="create_tournament",
    ),
    path(
        "",
        views.AllTournamentsView.as_view(),
        name="all_tournaments",
    ),
    path(
        "<int:tournament_id>/send_request_team_tournament",
        views.SendRequestToTournamentView.as_view(),
        name="send_request_team_tournament",
    ),
    path(
        "user_all_request_team_tournament",
        views.UserAllRequestTeamTournament.as_view(),
        name="user_all_request_team_tournament",
    ),
    path(
        "<int:tournament_id>/manage/battles",
        views.ManageBattleView.as_view(),
        name="manage_tournament_battles",
    ),
    path(
        "<int:tournament_id>/manage/battles/create",
        views.BattleCreateView.as_view(),
        name="create_battle",
    ),
    path(
        "tournament_reg_is_closed",
        TemplateView.as_view(
            template_name="includes/error.html",
            extra_context={
                "error_message": "Tournament Registration Teams is Closed",
            },
        ),
        name="tournament_reg_is_closed",
    ),
]
