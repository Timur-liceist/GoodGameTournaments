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
]
