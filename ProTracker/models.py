from django.db import models

# Create your models here.
class Team(models.Model):
    team_code = models.CharField(max_length = 3)
    team_name = models.CharField(max_length = 50)
    def __str__(self):
        return self.team_name

class Player(models.Model):
    player_ign = models.CharField(max_length = 30)
    player_name = models.CharField(max_length = 50)
    team = models.ForeignKey(Team, on_delete = models.CASCADE)
    def __str__(self):
        return self.player_ign

class PlayerAccount(models.Model):
    account_id = models.CharField(max_length = 78)
    account_name = models.CharField(max_length = 16)
    account_region = models.CharField(max_length = 4)
    player = models.ForeignKey(Player, on_delete = models.CASCADE)
    def __str__(self):
        return self.account_name + " (" + self.account_region + ")"

class MatchInfo(models.Model):
    match_id = models.CharField(max_length = 14)
    player = models.ForeignKey(Player, on_delete = models.CASCADE)