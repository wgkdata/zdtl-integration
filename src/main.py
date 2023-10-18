import requests as r
import json as j
from trello import Trello
from zendesk import Zendesk

trl = Trello()
zd = Zendesk()


def create_ticket_card(id):
    tk = zd.get_ticket(id)
    ticket_name = f"{id} - {tk['ticket']['subject']}"
    ticket_desc = tk['ticket']['description']

    response = trl.create_card(ticket_name, ticket_desc)

    if response == r.codes.ok:
        print(f'Card do ticket {id} criado com sucesso.')
# Test
