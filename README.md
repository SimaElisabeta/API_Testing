# API Testing Project

This project aims to automate the testing of an API. The project utilizes Postman, a popular API development and Pytest
Framework.

## Table of Contents

- [Overview](#overviewe)
    - [Intro](#intro)
    - [Tested Endpoints](#tested-endpoints)
- [Project Structure](#project-structure)
    - [Requests Directory](#requests-directory)
    - [Tests Directory](#tests-directory)
- [Dependencies](#dependencies)
- [How to Use](#how-to-use)
    - [Installation and Usage](#installation-and-usage)
    - [Test Results](#test-results)

## Overview

### Intro

This repository contains a Python automation application developed to test an online API
called [Simple Books API](https://simple-books-api.glitch.me). The application utilizes the pytest package and was
inspired by
the ["Introduction to Postman"](https://github.com/vdespa/introduction-to-postman-course/blob/main/simple-books-api.md)
course created by **vdespa**.

The **Simple Books API** allows you to reserve books and perform various operations such as retrieving book information,
submitting orders, and managing orders.

### Tested Endpoints

These are the following endpoints that I tested and that are available in the **Simple Books API**:

- `GET /status`: Returns the status of the API.
- `GET /books`: Returns a list of books. Optional query parameters can be used to filter the results.
- `GET /books/:bookId`: Retrieve detailed information about a book.
- `POST /orders`: Allows you to submit a new order. Requires authentication.
- `GET /orders`: Allows you to view all orders. Requires authentication.
- `GET /orders/:orderId`: Allows you to view an existing order. Requires authentication.
- `PATCH /orders/:orderId`: Update an existing order. Requires authentication.
- `DELETE /orders/:orderId`: Delete an existing order. Requires authentication.
- `POST /api-clients/`: Register your API client in order to receive an authentication token.

## Project Structure

The project is composed of the following directories:

- **requests**: Contains files for making API requests to different endpoints.
- **tests**: Contains test files for each endpoint to verify their functionality.

### Requests Directory

The requests directory contains the following files:

- `status.py`: Implements a function to retrieve the API status by making a GET request
  to `https://simple-books-api.glitch.me/status/`.
- `books.py`: Provides functions to interact with book-related endpoints, including retrieving all books and a specific
  book by ID.
- `api_clients.py`: Implements functions for API client authentication and token retrieval.
- `orders.py`: Includes functions to add, retrieve, edit, and delete orders, along with the necessary authorization
  headers.

### Tests Directory

The tests directory contains the following files:

- `test_status.py`: Contains test cases for the API status endpoint.
- `test_books.py`: Includes test cases for various book-related endpoints.
- `test_api_clients.py`: Provides test cases for API client authentication and token retrieval.
- `test_orders.py`: Contains test cases for different order-related endpoints.

## Dependencies

The project relies on the following dependencies:

- `requests`: Used for making HTTP requests to the API.
- `pytest`: The testing framework used to execute the test cases.

## How to Use

### Installation and Usage

To run the API tests locally, follow these steps:

1. Clone the repository to your local machine: \
   `git clone https://github.com/SimaElisabeta/API_Testing`
2. Install the required dependencies: \
   `pip install requests` \
   `pip install pytest`
3. Execute all test cases:
   `pytest books/tests/ -v`

### Test Results

The test cases were executed using pytest, and all 36 test cases passed successfully. The tests cover different
scenarios, including verifying status codes, error messages and JSON responses.

You should see similar output after all tests are run:

```
========================================================================================================== test session starts ===========================================================================================================
...
collected 36 items

books/tests/test_api_clients.py::TestApiClients::test_login_status_201 PASSED                                                                                                                                                       [  2%]
books/tests/test_api_clients.py::TestApiClients::test_login_token_exists PASSED                                                                                                                                                     [  5%]
books/tests/test_api_clients.py::TestApiClients::test_login_409 PASSED                                                                                                                                                              [  8%]
books/tests/test_api_clients.py::TestApiClients::test_login_invalid_email PASSED                                                                                                                                                    [ 11%]
books/tests/test_api_clients.py::TestApiClients::test_login_invalid_name PASSED                                                                                                                                                     [ 13%]
books/tests/test_books.py::TestBooks::test_get_books_200 PASSED                                                                                                                                                                     [ 16%]
books/tests/test_books.py::TestBooks::test_get_all_books_total PASSED                                                                                                                                                               [ 19%]
books/tests/test_books.py::TestBooks::test_get_all_books_limit PASSED                                                                                                                                                               [ 22%]
books/tests/test_books.py::TestBooks::test_get_all_books_type_fiction PASSED                                                                                                                                                        [ 25%]
books/tests/test_books.py::TestBooks::test_get_all_books_type_non_fiction PASSED                                                                                                                                                    [ 27%]
books/tests/test_books.py::TestBooks::test_get_all_books_type_and_limit PASSED                                                                                                                                                      [ 30%]
books/tests/test_books.py::TestBooks::test_get_all_books_invalid_type PASSED                                                                                                                                                        [ 33%]
books/tests/test_books.py::TestBooks::test_get_all_books_invalid_limit_negative_number PASSED                                                                                                                                       [ 36%]
books/tests/test_books.py::TestBooks::test_get_books_body PASSED                                                                                                                                                                    [ 38%]
books/tests/test_books.py::TestBooks::test_get_book PASSED                                                                                                                                                                          [ 41%]
books/tests/test_books.py::TestBooks::test_get_book_invalid_id PASSED                                                                                                                                                               [ 44%]
books/tests/test_orders.py::TestOrders::test_add_order_invalid_token PASSED                                                                                                                                                         [ 47%]
books/tests/test_orders.py::TestOrders::test_add_order_valid_book_id PASSED                                                                                                                                                         [ 50%]
books/tests/test_orders.py::TestOrders::test_add_order_invalid_book_id PASSED                                                                                                                                                       [ 52%]
books/tests/test_orders.py::TestOrders::test_add_order_book_out_of_stock PASSED                                                                                                                                                     [ 55%]
]
books/tests/test_orders.py::TestOrders::test_delete_order_unauth PASSED                                                                                                                                                             [ 83%]
]
books/tests/test_orders.py::TestOrders::test_edit_order_invalid_token PASSED                                                                                                                                                        [ 86%]
]
books/tests/test_orders.py::TestOrders::test_edit_order_valid_order_id PASSED                                                                                                                                                       [ 88%]
]
books/tests/test_orders.py::TestOrders::test_edit_order_invalid_order_id PASSED                                                                                                                                                     [ 91%]
]
books/tests/test_orders.py::TestOrders::test_delete_order_unauth PASSED                                                                                                                                                             [ 83%] 
books/tests/test_orders.py::TestOrders::test_edit_order_invalid_token PASSED                                                                                                                                                        [ 86%] 
books/tests/test_orders.py::TestOrders::test_edit_order_valid_order_id PASSED                                                                                                                                                       [ 88%] 
books/tests/test_orders.py::TestOrders::test_edit_order_invalid_order_id PASSED                                                                                                                                                     [ 91%] 
books/tests/test_orders.py::TestOrders::test_edit_order_unauth PASSED                                                                                                                                                               [ 94%] 
books/tests/test_status.py::TestStatus::test_status_code_200 PASSED                                                                                                                                                                 [ 97%] 
books/tests/test_status.py::TestStatus::test_status_body PASSED                                                                                                                                                                     [100%] 

========================================================================================================== 36 passed in 53.18s =========================================================================================================== 
...
```
