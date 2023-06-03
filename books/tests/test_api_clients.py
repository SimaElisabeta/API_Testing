from books.requests.api_clients import *
from random import randint


class TestApiClients:
    nr = randint(1, 9999999)
    client_name = 'Test'
    client_email = f'test_mail{nr}@example.com'
    response = login(client_name=client_name, client_email=client_email)

    # Test the login POST method to create a new user adn check if the new client has a token in the body
    def test_login_status_201(self):
        assert self.response.status_code == 201, 'Status code is not ok'

    def test_login_token_exists(self):
        r = self.response.json()
        assert 'accessToken' in r, 'Accesstoken does not exists'

    def test_login_409(self):
        self.response = login(self.client_name, self.client_email)
        error_msg = self.response.json()['error']
        assert self.response.status_code == 409, 'Status code is not ok'
        assert error_msg == "API client already registered. Try a different email.", 'Wrong error message'

    def test_login_invalid_email(self):
        self.response = login(self.client_name, 'invalid_mail')
        error_msg = self.response.json()['error']
        assert self.response.status_code == 400, 'Status code is not ok'
        assert error_msg == "Invalid or missing client email.", 'Wrong error message'

    def test_login_invalid_name(self):
        self.response = login('', self.client_email)
        error_msg = self.response.json()['error']
        assert self.response.status_code == 400, 'Status code is not ok'
        assert error_msg == "Invalid or missing client name.", 'Wrong error message'
