import pytest
import sender_stand_request
import data

def test_assert_by_order_track_can_get_order_data():
    new_order_response = sender_stand_request.post_create_new_order(data.order_body)
   # print(new_order_response.json()["track"])
    order_data_response = sender_stand_request.get_order_data(new_order_response.json()["track"])
    # Проверяется, что код ответа равен 200
    assert order_data_response.status_code == 200

