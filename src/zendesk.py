import requests as r 
import json as j

class Zendesk:
    def __init__(self):
        self.user = 'your@email/token'
        self.token = 'YOURAPITOKEN'
        self.surl = 'https://yourdomain.zendesk.com/api/v2'
        self.headers = {
            'content-type': 'application/json'
        }

    def get_ticket(self, id):
        url = f'{self.surl}/tickets/{id}'

        response = r.request('GET', url, auth=(self.user, self.token), headers=self.headers)

        ticket = j.loads(response.text)
                
        return ticket
