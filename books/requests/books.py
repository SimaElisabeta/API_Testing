import requests


def get_all_books(book_type='', limit=''):
    response = requests.get(f'https://simple-books-api.glitch.me/books?type={book_type}&limit={limit}/')
    return response


def get_book(id):
    response = requests.get(f'https://simple-books-api.glitch.me/books/{id}')
    return response


if __name__ == '__main__':
    pass
