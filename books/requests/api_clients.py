import requests
from random import randint


# This method is tested in test_api_clients
def login(client_name=None, client_email=None):
    json = {
        "clientName": client_name,
        "clientEmail": client_email
    }

    response = requests.post('https://simple-books-api.glitch.me/api-clients/', json=json)
    return response


# This method is tested in test_orders
def get_token():
    # Creates a new user for every get_token() call and returns the token
    nr = randint(1, 9999999)
    json = {
        "clientName": 'Test',
        "clientEmail": f'test_mail{nr}@example.com'
    }

    response = requests.post('https://simple-books-api.glitch.me/api-clients/', json=json)
    return response.json()['accessToken']
