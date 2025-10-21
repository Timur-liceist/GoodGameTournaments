from teams.models import TeamModel


def is_leader_for_team(user_id, team_id):
    team = TeamModel.objects.filter(id=team_id).first()
    return team.leader.id == user_id
