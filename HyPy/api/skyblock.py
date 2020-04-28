import requests
from HyPy.main import random_api_key, hypixel_url, success
from HyPy.errors import BazaarNotFound, AucitionNotFound, NoArguments, ProfileNotFound, NewsNotFound
from .player import Player


class Skyblock:
    @staticmethod
    def auction(player=None, profile=None, uuid=None):
        if player is not None:
            link = requests.get(f'{hypixel_url}skyblock/auction{random_api_key()}&player={player}').json()
        elif profile is not None:
            link = requests.get(f'{hypixel_url}skyblock/auction{random_api_key()}&profile={profile}').json()
        elif uuid is not None:
            link = requests.get(f'{hypixel_url}skyblock/auction{random_api_key()}&uuid={uuid}').json()
        else:
            raise NoArguments
        if not success(link):
            raise AucitionNotFound
        return link

    @staticmethod
    def auctions(page=0):
        link = requests.get(f'{hypixel_url}skyblock/auctions{random_api_key()}&page={page}').json()
        if not success(link):
            raise AucitionNotFound
        return link

    @staticmethod
    def bazaar():
        link = requests.get(f'{hypixel_url}skyblock/bazaar{random_api_key()}').json()
        if not success(link):
            raise BazaarNotFound
        return link

    @staticmethod
    def news():
        link = requests.get(f'{hypixel_url}skyblock/news{random_api_key()}').json()
        if not success(link):
            raise NewsNotFound
        return link

    @staticmethod
    def profile():
        link = requests.get(f'{hypixel_url}skyblock/profile{random_api_key()}').json()
        if not success(link):
            raise ProfileNotFound
        return link

    @staticmethod
    def product(product_id):
        link = requests.get(f'{hypixel_url}skyblock/bazaar/product{random_api_key()}').json()
        if not success(link):
            raise BazaarNotFound
        return link

    @staticmethod
    def products():
        link = requests.get(f'{hypixel_url}skyblock/bazaar/products{random_api_key()}').json()
        if not success(link):
            raise BazaarNotFound
        return link


class Profile:
    def __init__(self, **kwargs):
        if kwargs['username']:
            data = Player.player(username=kwargs['username'])
            for profile in data['player']['stats']['SkyBlock']['profiles']:
                if data['player']['stats']['SkyBlock']['profiles'][profile]['cute_name'] != kwargs['cute_name']:
                    continue
                else:
                    self.profile_id = data['player']['stats']['SkyBlock']['profiles'][profile]['profile_id']
                    self.cute_name = kwargs['cute_name']
                    break
        elif kwargs['profile_id']:
            self.profile_id = kwargs['profile_id']
            link = requests.get(
                f'{hypixel_url}skyblock/profile{random_api_key()}&profile={kwargs["profile_id"]}').json()
        else:
            raise NoArguments

    def users(self):
        link = requests.get(f'{hypixel_url}skyblock/profile{random_api_key()}&profile={self.profile_id}').json()
        if not success(link):
            raise ProfileNotFound
        return link['profile']['members']
