from django.urls import path

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
        "all_request_team_tournament",
        views.SendRequestToTournamentView.as_view(),
        name="all_request_team_tournament",
    ),
]
