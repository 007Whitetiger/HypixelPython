import random
import requests
from .errors import NoArguments

hypixel_url = 'https://api.hypixel.net/'
uuid_url = 'https://api.mojang.com/users/profiles/minecraft/'
username_url = 'https://api.mojang.com/user/profiles/{}/names'


def success(response):
    if response['success']:
        return True
    else:
        return False


def random_api_key():
    random_key = random.choice(Api.api_keys)
    random_key = '?key=' + random_key
    return random_key


class Api:
    api_keys = []

    def __init__(self, api_key):
        link = requests.get(f'{hypixel_url}key?key={api_key}').json()
        if not success(link):
            raise NoArguments
        self.api_keys.append(api_key)

    def addkey(self, key):
        link = requests.get(f'{hypixel_url}key{random_api_key()}&key={key}').json()
        if not success(link):
            raise NoArguments
        self.api_keys.append(key)


from HyPy.api import Player, Skyblock, Guild, general, Profile