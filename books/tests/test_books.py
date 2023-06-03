from books.requests.books import *


class TestBooks:
    # Test cases for all books
    def test_get_books_200(self):
        r = get_all_books()
        assert r.status_code == 200, 'Status get books code is not ok'

    def test_get_all_books_total(self):
        json_r = get_all_books().json()
        books_total = len(json_r)
        assert books_total == 6, 'Books total is wrong'

    def test_get_all_books_limit(self):
        json_r = get_all_books(limit=3).json()
        books_total = len(json_r)
        assert books_total == 3, 'Books total limit is wrong'

    def test_get_all_books_type_fiction(self):
        json_r = get_all_books(book_type='fiction').json()
        books_total = len(json_r)
        assert books_total == 4, 'Book type fiction is wrong'

    def test_get_all_books_type_non_fiction(self):
        json_r = get_all_books(book_type='non-fiction').json()
        books_total = len(json_r)
        assert books_total == 2, 'Book type non-fiction is wrong'

    def test_get_all_books_type_and_limit(self):
        json_r = get_all_books(book_type='fiction', limit=2).json()
        books_total = len(json_r)
        assert json_r[0]['type'] == 'fiction', 'Book type fiction is wrong'
        assert books_total == 2, 'Book total for type fiction and limit is wrong'

    def test_get_all_books_invalid_type(self):
        r = get_all_books(book_type='abc')
        json_r = r.json()
        error_msg = json_r['error']
        assert r.status_code == 400, 'Status code is not ok'
        assert error_msg == "Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction.", 'Wrong error message'

    def test_get_all_books_invalid_limit_negative_number(self):
        r = get_all_books(limit=-1)
        json_r = r.json()
        error_msg = json_r['error']
        assert r.status_code == 400, 'Status code is not ok'
        assert error_msg == "Invalid value for query parameter 'limit'. Must be greater than 0.", 'Wrong error message'

    def test_get_books_body(self):
        book = get_all_books().json()[0]
        expected_book = {
            "id": 1,
            "name": "The Russian",
            "type": "fiction",
            "available": True
        }
        assert book == expected_book, 'Book body data is not ok'

    # Test cases for specific book id
    def test_get_book(self):
        r = get_book(1)
        expected = {
            "id": 1,
            "name": "The Russian",
            "author": "James Patterson and James O. Born",
            "isbn": "1780899475",
            "type": "fiction",
            "price": 12.98,
            "current-stock": 12,
            "available": True
        }
        assert r.status_code == 200, 'Status code is not ok'
        assert r.json() == expected, 'Book body data is not ok'

    def test_get_book_invalid_id(self):
        r = get_book(234)
        error_msg = r.json()['error']
        assert r.status_code == 404, 'Status code is not ok'
        assert error_msg == 'No book with id 234', 'Wrong error message'
