from django.db import models

# Create your models here.
class Team(models.Model):
    team_id = models.CharField(max_length = 3)
    team_name = models.CharField(max_length = 50)
    def __str__(self):
        return "[" + self.team_id + "] " + self.team_name

class Player(models.Model):
    player_ID = models.CharField(max_length = 6)
    player_ign = models.CharField(max_length = 30)
    player_name = models.CharField(max_length = 50)
    team = models.ForeignKey(Team, on_delete = models.CASCADE)

class PlayerAccount(models.Model):
    account_id = models.CharField(max_length = 78)
    player = models.ForeignKey(Player, on_delete = models.CASCADE)
