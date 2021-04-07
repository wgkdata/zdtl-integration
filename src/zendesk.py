import requests as r 
import json as j
import os

current_dir = os.getcwd()

CREDENTIALS = current_dir + "/creds/04062021.json"

data = j.load(open(CREDENTIALS, 'r'))

class Zendesk:
    def __init__(self):
        self.user = data['zendesk']['user']
        self.token = data['zendesk']['token']
        self.baseurl = data['zendesk']['baseurl']
        self.headers = {
            'content-type': 'application/json'
        }

    def get_ticket(self, id):
        url = f'{self.baseurl}/tickets/{id}'

        response = r.request('GET', url, auth=(self.user, self.token), headers=self.headers)

        ticket = j.loads(response.text)
                
        return ticket
