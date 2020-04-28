import requests
from HyPy.errors import (PlayerNotFound, NoArguments, GuildNotFound, FriendsNotFound, PlayerCountNotFound,
                         RecentGamesNotFound)
from HyPy.main import success, hypixel_url, uuid_url, username_url, random_api_key


class Player:
    def __init__(self, username=None, uuid=None):
        if username is None:
            self.username = requests.get(username_url.format(uuid)).json()
            number = len(self.username)
            number = number - 1
            self.username = self.username[number]['name']
            self.uuid = uuid
        elif uuid is None:
            self.username = username
            self.uuid = requests.get(f'{uuid_url}{username}').json()['id']
        else:
            raise NoArguments

    @staticmethod
    def player(username=None, uuid=None):
        if username is not None:
            uuid = requests.get(f'{uuid_url}{username}').json()['id']

        link = requests.get(f'{hypixel_url}player{random_api_key()}&uuid={uuid}').json()
        if not success(link):
            raise PlayerNotFound
        return link

    def __repr__(self):
        link = requests.get(f'{hypixel_url}player{random_api_key()}&uuid={self.uuid}').json()
        if not success(link):
            raise PlayerNotFound
        return link

    def friends(self, raw=False):
        link = requests.get(f'{hypixel_url}friends{random_api_key()}&uuid={self.uuid}').json()
        if not success(link):
            raise FriendsNotFound
        x = 0
        if raw:
            return link
        elif not raw:
            while x < len(link['records']):
                friends = {}
                uuid = link['records'][x]['uuidReceiver']
                player = self.player(uuid=uuid)
                friends[player['player']['playername']] = player
                x += 1
            return friends

    def guild(self):
        link = requests.get(f'{hypixel_url}guild{random_api_key()}&player={self.uuid}').json()
        if not success(link):
            raise GuildNotFound
        return link

    def status(self):
        link = requests.get(f'{hypixel_url}status{random_api_key()}&uuid={self.uuid}').json()
        if not success(link):
            raise PlayerCountNotFound
        return link

    def recentGames(self):
        link = requests.get(f'{hypixel_url}recentGames{random_api_key()}&uuid={self.uuid}').json()
        if not success(link):
            raise RecentGamesNotFound
        return link
