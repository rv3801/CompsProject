from riotwatcher import LolWatcher
import os

api_key_file = open("ProTracker\API_Key.txt", "r")
api_key = api_key_file.read()
lol_watcher = LolWatcher(api_key)

my_region = 'na1'

def get_info():
    me = lol_watcher.summoner.by_name(my_region, 'temp3801')
    return me["summonerLevel"]
