from .models import *

def add_team(team_code, team_name):
    new_team = Team(team_code = team_code, team_name = team_name)
    new_team.save()

liquid = add_team("TL", "Team Liquid")