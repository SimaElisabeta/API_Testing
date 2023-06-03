import requests


def get_status():
    return requests.get('https://simple-books-api.glitch.me/status/')


if __name__ == '__main__':
    pass
