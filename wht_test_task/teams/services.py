from teams.models.team import TeamModel
from teams.models.person import PersonModel


def add_team_member(team_id: int, member_id: int) -> None:
    team = TeamModel.objects.get(id=team_id)
    member = PersonModel.objects.get(id=member_id)
    team.members.add(member)


def remove_team_member(team_id: int, member_id: int) -> None:
    team = TeamModel.objects.get(id=team_id)
    member = PersonModel.objects.get(id=member_id)
    team.members.remove(member)
