from riotwatcher import LolWatcher
import os

api_key_file = open("ProTracker\API_Key.txt", "r")
api_key = api_key_file.read()
lol_watcher = LolWatcher(api_key)

my_region = 'na1'

def get_summoner_level(region, summoner_name):
    me = lol_watcher.summoner.by_name(region, summoner_name)
    return me["summonerLevel"]
