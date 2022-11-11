from django.shortcuts import render
from django.http import HttpResponse
from .RiotWatcher import get_info
from .models import *

# Create your views here.
def index(request):
    # return HttpResponse("Hello, world. You're at the ProTracker index.")
    team_list = Team.objects.order_by('team_code')
    my_info = get_info
    context = {'team_list': team_list, 'my_info' : my_info}
    return render(request, 'ProTracker/index.html', context)

def team(request, team_code):
    team = Team.objects.get(team_code = team_code)
    player_list = Player.objects.filter(team = team)
    context = {'team': team, 'player_list': player_list}
    return render(request, 'ProTracker/team.html', context)

def player(request, player_ign):
    player = Player.objects.get(player_ign = player_ign)
    # response = "You are looking at the player page for %s."
    # return HttpResponse(response % player)
    player_accts_list = PlayerAccount.objects.filter(player = player)
    context = {'player' : player, 'player_accts_list' : player_accts_list}
    return render(request, 'ProTracker/player.html', context)