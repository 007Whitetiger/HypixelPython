import requests
from HyPython.main import random_api_key, success, hypixel_url, uuid_url
from HyPython.errors import GuildNotFound, NoArguments, PlayerCountNotFound, KeyNotFound, LeaderboardNotFound, \
    RecentGamesNotFound, RecourcesNotFound, WatchsdogStatsNotFound, FriendsNotFound, PlayerNotFound
from .player import Player


def boosters():
    link = requests.get(f'{hypixel_url}boosters{random_api_key()}').json()
    if not success(link):
        raise
    return link


def findGuild(byname=False, byuuid=False):
    if isinstance(byname, str):
        link = requests.get(f'{hypixel_url}findGuild{random_api_key()}&byName={byname}').json()
    elif isinstance(byuuid, str):
        link = requests.get(f'{hypixel_url}findGuild{random_api_key()}&byUuid={byuuid}').json()
    else:
        raise NoArguments
    if not success(link):
        raise GuildNotFound
    return link


def gameCounts():
    link = requests.get(f'{hypixel_url}gameCounts{random_api_key()}').json()
    if not success(link):
        raise PlayerCountNotFound
    return link


def guild(id=False, player=False, name=False):
    if isinstance(id, str):
        link = requests.get(f'{hypixel_url}guild{random_api_key()}&id={id}').json()
    elif isinstance(player, str):
        link = requests.get(f'{hypixel_url}guild{random_api_key()}&player={player}').json()
    elif isinstance(name, str):
        link = requests.get(f'{hypixel_url}guild{random_api_key()}&name={name}').json()
    else:
        raise NoArguments
    if not success(link):
        raise GuildNotFound
    return link


def key(key=None):
    if key is None:
        link = requests.get(f'{hypixel_url}key{random_api_key()}&key={key}').json()
    else:
        link = requests.get(f'{hypixel_url}key{random_api_key()}')
    if not success(link):
        raise KeyNotFound
    return link


def leaderboard():
    link = requests.get(f'{hypixel_url}leaderboard{random_api_key()}').json()
    if not success(link):
        raise LeaderboardNotFound
    return link


def playerCount():
    link = requests.get(f'{hypixel_url}playerCount{random_api_key()}').json()
    if not success(link):
        raise PlayerCountNotFound
    return link


def recentGames(username=None, uuid=None):
    player = Player.player(username=username, uuid=uuid)
    link = requests.get(f'{hypixel_url}recentGames{random_api_key()}&uuid={player["player"]["_id"]}').json()
    if not success(link):
        raise RecentGamesNotFound
    return link


def recources(achievements=None, challenges=None, quests=None, guilds_achievements=None,
              guilds_permissions=None, skyblock_collections=None, skyblock_skills=None):
    if achievements is not None:
        link = requests.get(f'{hypixel_url}recources/achievements').json()
    elif challenges is not None:
        link = requests.get(f'{hypixel_url}recources/challenges').json()
    elif quests is not None:
        link = requests.get(f'{hypixel_url}recources/quests').json()
    elif guilds_achievements is not None:
        link = requests.get(f'{hypixel_url}recources/guild/achievements').json()
    elif guilds_permissions is not None:
        link = requests.get(f'{hypixel_url}recources/guild/permissions').json()
    elif skyblock_collections is not None:
        link = requests.get(f'{hypixel_url}recources/skyblock/collections').json()
    elif skyblock_skills is not None:
        link = requests.get(f'{hypixel_url}recources/skyblock/skills').json()
    else:
        raise NoArguments
    if not success(link):
        raise RecourcesNotFound
    return link


def watchdogstats():
    link = requests.get(f'{hypixel_url}watchdogstats{random_api_key()}').json()
    if not success(link):
        raise WatchsdogStatsNotFound
    return link


def friends(username=None, uuid=None, raw=False):
    if uuid is None:
        uuid = requests.get(f'{uuid_url}{username}').json()
        link = requests.get(f'{hypixel_url}friends{random_api_key()}&uuid={uuid["id"]}').json()
    elif uuid is not None:
        link = requests.get(f'{hypixel_url}friends{random_api_key()}&uuid={uuid}').json()
    else:
        raise NoArguments
    if not success(link):
        raise FriendsNotFound
    x = 0
    if raw:
        return link
    elif not raw:
        while x < len(link['records']):
            friends = {}
            uuid = link['records'][x]['uuidReceiver']
            player = Player.player(uuid=uuid)
            friends[player['player']['playername']] = player
            x += 1
        return friends


def player(username=None, uuid=None):
    if username is not None:
        uuid = requests.get(f'{uuid_url}{username}').json()['id']

    link = requests.get(f'{hypixel_url}player{random_api_key()}&uuid={uuid}').json()
    if not success(link):
        raise PlayerNotFound
    return link
