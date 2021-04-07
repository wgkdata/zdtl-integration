import requests as r 
import json as j
import pprint as p
import os

current_dir = os.getcwd()

CREDENTIALS = current_dir + "/creds/04062021.json"

data = j.load(open(CREDENTIALS, 'r'))

class Trello:
    def __init__(self):
        self.key = data['trello']['key']
        self.token = data['trello']['token']
        self.board = data['trello']['board']
        self.list = data['trello']['list']
        self.baseurl = 'https://api.trello.com/1'
        self.query = {
            'key': self.key,
            'token': self.token
        }
    
    def get_board(self):
        url = f'{self.baseurl}/boards/{self.board}'

        response = r.request('GET', url, params=self.query)
        
        p.pprint(j.loads(response.text))
    
    def get_board_cards(self):
        url = f'{self.baseurl}/boards/{self.board}/cards'

        response = r.request('GET', url, params=self.query)
        
        p.pprint(j.loads(response.text))
    
    def get_board_lists(self):
        url = f'{self.baseurl}/boards/{self.board}/lists'

        response = r.request('GET', url, params=self.query)
        
        p.pprint(j.loads(response.text))

    def get_card(self):
        card = 'CARDID'

        url = f'{self.baseurl}/cards/{card}'

        response = r.request('GET', url, params=self.query)
        
        p.pprint(j.loads(response.text))

    def create_card(self, name, desc):
        url = f'{self.baseurl}/cards/'

        query = {
            'key': self.key,
            'token': self.token,
            'idList': self.list,
            'name': name,
            'desc': desc
        }

        response = r.request('POST', url, params=query)
        
        return response.status_code
