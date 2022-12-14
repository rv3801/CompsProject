from django.shortcuts import render
from django.http import HttpResponse
from .models import Team, Player

# Create your views here.
def index(request):
    # return HttpResponse("Hello, world. You're at the ProTracker index.")
    team_list = Team.objects.order_by('team_id')
    context = {'team_list': team_list}
    return render(request, 'ProTracker/index.html', context)

def team(request, team_id):
    team = Team.objects.get(team_id = team_id)
    player_list = Player.objects.filter(team_id = team)
    context = {'team': team, 'player_list': player_list}
    return render(request, 'ProTracker/team.html', context)

def player(request, player_ign):
    player = Player.objects.get(player_ign = player_ign)
    response = "You are looking at the player page for %s."
    return HttpResponse(response % player)