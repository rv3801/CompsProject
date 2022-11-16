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
    match_region = models.CharField(max_length = 4, null = True)
    match_start_time = models.PositiveBigIntegerField(null = True)
    match_duration = models.PositiveSmallIntegerField(null = True)

class MatchParticipants(models.Model):
    match_id = models.ForeignKey(MatchInfo, on_delete = models.CASCADE)
    player = models.ForeignKey(Player, on_delete = models.CASCADE)
    champ_id = models.PositiveSmallIntegerField()
    # Primary Runes
    primary_rune = models.PositiveSmallIntegerField()
    primary_rune_slot_1 = models.PositiveSmallIntegerField()
    primary_rune_slot_2 = models.PositiveSmallIntegerField()
    primary_rune_slot_3 = models.PositiveSmallIntegerField()
    # Secondary Runes
    secondary_rune = models.PositiveSmallIntegerField()
    secondary_rune_slot_1 = models.PositiveSmallIntegerField()
    secondary_rune_slot_2 = models.PositiveSmallIntegerField()
    secondary_rune_slot_3 = models.PositiveSmallIntegerField()
    # Summoner Spells
    summoner_spell_1 = models.PositiveSmallIntegerField()
    summoner_spell_2 = models.PositiveSmallIntegerField()

class MatchParticipantItems(models.Model):
    match_id = models.ForeignKey(MatchInfo, on_delete = models.CASCADE)
    player = models.ForeignKey(Player, on_delete = models.CASCADE)
    item_id = models.PositiveSmallIntegerField()
