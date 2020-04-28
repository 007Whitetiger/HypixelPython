import requests
from HyPython.errors import NoArguments, GuildNotFound
from HyPython.main import success, hypixel_url, random_api_key


class Guild:
    def __init__(self, id=None, player=None, name=None):

        if id is not None:
            link = requests.get(f'{hypixel_url}guild{random_api_key()}&id={id}').json()
            self.name = link['guild']['name']
            self.id = id
        elif player is not None:
            link = requests.get(f'{hypixel_url}guild{random_api_key()}&player={player}').json()
            self.name = link['guild']['name']
            self.id = link['guild']['_id']
        elif name is not None:
            link = requests.get(f'{hypixel_url}guild{random_api_key()}&name={name}').json()
            self.name = name
            self.id = link['guild']['_id']
        else:
            raise NoArguments
        if not success(link):
            raise GuildNotFound

    def __repr__(self):
        link = requests.get(f'{hypixel_url}guild{random_api_key()}&id={self.id}').json()
        if not success(link):
            raise GuildNotFound
        return str(link)
