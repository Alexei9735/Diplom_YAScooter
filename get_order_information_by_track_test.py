import create_orders

def test_positive_assert():
    response = create_orders.get_receive_order_track()
    assert response.status_code == 200