from tournaments.models import TournamentModel


def is_owner_tournament(
    tournament_id=None,
    user_id=None,
    user=None,
    tournament=None,
):
    if not ((tournament or tournament_id) and (user_id or user)):
        error_message = "Missing agrument tournament or user"
        raise TypeError(error_message)

    if tournament_id:
        tournament = TournamentModel.filter(id=tournament_id).first()

    if user_id:
        user = TournamentModel.filter(id=user_id).first()

