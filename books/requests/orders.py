import requests
from requests.structures import CaseInsensitiveDict


# POST
def add_order(token, book_id, customer_name):
    # header for authorization
    headers = CaseInsensitiveDict()
    headers['Accept'] = 'application/json'
    headers['Authorization'] = f'Bearer {token}'

    # body
    json = {
        "bookId": book_id,
        "customerName": customer_name
    }

    response = requests.post('https://simple-books-api.glitch.me/orders/', headers=headers, json=json)
    return response


# GET ALL
def get_orders(token):
    # header for authorization
    headers = CaseInsensitiveDict()
    headers['Accept'] = 'application/json'
    headers['Authorization'] = f'Bearer {token}'

    response = requests.get('https://simple-books-api.glitch.me/orders/', headers=headers)
    return response


# GET
def get_order(token, order_id):
    # header for authorization
    headers = CaseInsensitiveDict()
    headers['Accept'] = 'application/json'
    headers['Authorization'] = f'Bearer {token}'

    response = requests.get(f'https://simple-books-api.glitch.me/orders/{order_id}/', headers=headers)
    return response


# PATCH
def edit_order(token, order_id, update_customer_name):
    # header for authorization
    headers = CaseInsensitiveDict()
    headers['Accept'] = 'application/json'
    headers['Authorization'] = f'Bearer {token}'

    # body
    json = {
        "customerName": update_customer_name
    }

    response = requests.patch(f'https://simple-books-api.glitch.me/orders/{order_id}/', headers=headers, json=json)
    return response


# DELETE
def delete_order(token, order_id):
    # header for authorization
    headers = CaseInsensitiveDict()
    headers['Accept'] = 'application/json'
    headers['Authorization'] = f'Bearer {token}'

    response = requests.delete(f'https://simple-books-api.glitch.me/orders/{order_id}/', headers=headers)
    return response
