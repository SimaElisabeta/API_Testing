from books.requests.orders import *
from books.requests.api_clients import *


class TestOrders:

    def setup_method(self):
        self.token = get_token()
        self.token2 = get_token()

    # ADD order test
    def test_add_order_invalid_token(self):
        r = add_order('invalid_token', 'Test', 'Test')
        error_msg = r.json()['error']
        assert r.status_code == 401, 'Status code is not ok'
        assert error_msg == "Invalid bearer token.", 'Wrong error message'

    def test_add_order_valid_book_id(self):
        r = add_order(self.token, 1, 'Eli')
        assert r.status_code == 201, 'Status code is not ok'
        assert r.json()['created'] is True, 'Order not created'

        # cleanup
        delete_order(self.token, r.json()['orderId'])

    def test_add_order_invalid_book_id(self):
        r = add_order(self.token, 700, 'Eli')
        error_msg = r.json()['error']

        assert r.status_code == 400, 'Status code is not ok'
        assert error_msg == "Invalid or missing bookId.", 'Wrong error message'

    def test_add_order_book_out_of_stock(self):
        r = add_order(self.token, 2, 'Eli')
        error_msg = r.json()['error']

        assert r.status_code == 404, 'Status code is not ok'
        assert error_msg == "This book is not in stock. Try again later.", 'Wrong error message'

    # GET orders test
    def test_get_orders_invalid_token(self):
        r = get_orders('invalid_token')
        error_msg = r.json()['error']
        assert r.status_code == 401, 'Status code is not ok'
        assert error_msg == "Invalid bearer token.", 'Wrong error message'

    def test_get_orders(self):
        orders = [add_order(self.token, 1, 'Eli'), add_order(self.token, 1, 'Eli')]
        r = get_orders(self.token)
        assert r.status_code == 200, 'Status code is not ok'
        assert len(r.json()) == len(orders), 'Get orders not working'

        # cleanup
        for order in orders:
            delete_order(self.token, order.json()['orderId'])

    # GET order test
    def test_get_order_invalid_token(self):
        r = get_order('invalid_token', 'Test')
        error_msg = r.json()['error']
        assert r.status_code == 401, 'Status code is not ok'
        assert error_msg == "Invalid bearer token.", 'Wrong error message'

    def test_get_order_valid_order_id(self):
        orders = [add_order(self.token, book_id=1, customer_name='Test'),
                  add_order(self.token, book_id=1, customer_name='Eli')]
        order1_id = orders[0].json()['orderId']
        r = get_order(self.token, order1_id)

        assert r.status_code == 200, 'Status code is not ok'
        assert r.json()['id'] == order1_id, 'Id is not ok'
        assert r.json()['bookId'] == 1, 'Book Id is not ok'
        assert r.json()['customerName'] == 'Test', 'Customer Name is not ok'
        assert r.json()['quantity'] == 1, 'Quantity is not ok'

        # cleanup
        for order in orders:
            delete_order(self.token, order.json()['orderId'])

    def test_get_order_invalid_order_id(self):
        r = get_order(self.token, 'invalid_order_id')
        error_msg = r.json()['error']
        assert r.status_code == 404, 'Status code is not ok'
        assert error_msg == "No order with id invalid_order_id.", 'Wrong error message'

    def test_get_order_unauth(self):
        new_order = add_order(self.token, 1, 'Eli')
        order_id = new_order.json()['orderId']

        r = get_order(self.token2, order_id)

        error_msg = r.json()['error']
        assert r.status_code == 404, 'Status code is not ok'
        assert error_msg == f"No order with id {order_id}.", 'Wrong error message'

        # cleanup
        delete_order(self.token, order_id)

    # DELETE order test
    def test_delete_order_invalid_token(self):
        r = add_order('invalid_token', 'Test', 'Test')
        error_msg = r.json()['error']
        assert r.status_code == 401, 'Status code is not ok'
        assert error_msg == "Invalid bearer token.", 'Wrong error message'

    def test_delete_order_valid_order_id(self):
        new_order = add_order(self.token, 1, 'Eli')
        order_id = new_order.json()['orderId']
        r = delete_order(self.token, order_id)
        assert r.status_code == 204, 'Status code is not ok'
        get_all = get_orders(self.token)
        assert len(get_all.json()) == 0, 'Order was not deleted'

    def test_delete_order_invalid_order_id(self):
        r = delete_order(self.token, 'invalid_order_id')
        error_msg = r.json()['error']
        assert r.status_code == 404, 'Status code is not ok'
        assert error_msg == "No order with id invalid_order_id.", 'Wrong error message'

    def test_delete_order_unauth(self):
        new_order = add_order(self.token, 1, 'Eli')
        order_id = new_order.json()['orderId']

        r = delete_order(self.token2, order_id)

        error_msg = r.json()['error']
        assert r.status_code == 404, 'Status code is not ok'
        assert error_msg == f"No order with id {order_id}.", 'Wrong error message'

        # cleanup
        delete_order(self.token, order_id)

    # EDIT order test
    def test_edit_order_invalid_token(self):
        r = edit_order('invalid_token', 'Test', 'Test')
        error_msg = r.json()['error']

        assert r.status_code == 401, 'Status code is not ok'
        assert error_msg == "Invalid bearer token.", 'Wrong error message'

    def test_edit_order_valid_order_id(self):
        new_order = add_order(self.token, 1, 'Eli')
        order_id = new_order.json()['orderId']

        update_customer = 'Elisabeta'
        r = edit_order(self.token, order_id, update_customer)

        assert r.status_code == 204, 'Status code is not ok'
        check_if_update = get_order(self.token, order_id).json()['customerName']
        assert check_if_update == 'Elisabeta', 'Edit name is not working'

        # cleanup
        delete_order(self.token, order_id)

    def test_edit_order_invalid_order_id(self):
        r = edit_order(self.token, 'invalid_order_id', 'Test')
        error_msg = r.json()['error']
        assert r.status_code == 404, 'Status code is not ok'
        assert error_msg == "No order with id invalid_order_id.", 'Wrong error message'

    def test_edit_order_unauth(self):
        new_order = add_order(self.token, 1, 'Eli')
        order_id = new_order.json()['orderId']

        update_customer = 'Elisabeta'
        r = edit_order(self.token2, order_id, update_customer)

        error_msg = r.json()['error']
        assert r.status_code == 404, 'Status code is not ok'
        assert error_msg == f"No order with id {order_id}.", 'Wrong error message'

        # cleanup
        delete_order(self.token, order_id)
