from books.requests.status import *


class TestStatus:

    def test_status_code_200(self):
        assert get_status().status_code == 200, 'status code is not ok'

    def test_status_body(self):
        assert get_status().json()['status'] == 'OK', 'status msg is not ok'
