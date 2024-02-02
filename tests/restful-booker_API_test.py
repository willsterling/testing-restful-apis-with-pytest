import requests
from approvaltests.approvals import verify
from api_calls.restfulbooker_request_calls import new_auth, create_token,get_booking_ids,get_booking,create_booking,update_booking,partial_update_booking, delete_booking


from config import BOOKER_URI


# SECTION: Tests

def get_booking_id():
    response_for_create_booking = create_booking()
    data = response_for_create_booking.json()
    return data["bookingid"]

# HealthCheck
def test_healthcheck_resp_booker():
    # healthcheck endpoint to confirm API is up and running
    response = requests.get(BOOKER_URI + '/ping')
    assert response.status_code == 201

# GetBooking
def test_get_booking():
    booking_id = get_booking_id()

    # get booking from booking id
    response_for_get_booking = get_booking(booking_id)
    assert response_for_get_booking.status_code == 200
    booking = response_for_get_booking.json()

    #assertions for data validation:
    assert booking['firstname'] == 'Jacques'
    assert booking['lastname'] == 'Revolt'
    assert booking['totalprice'] == 1200


# CreateToken
def test_can_create_token():
    # send post request of username and password to create a random token. Assert response is 200
    # auth = new_auth()
    response_for_create_token = create_token()
    assert response_for_create_token.status_code == 200
    data = response_for_create_token.json()

    # verify token is created and is the standard length of 15 characters
    a_token = data['token']
    assert len(a_token) == 15


# GetBookingIds
def test_get_all_bookingids():
    response_for_get_booking_ids = get_booking_ids()
    assert response_for_get_booking_ids.status_code == 200
    booking_ids = response_for_get_booking_ids.json()

    # To see the response data, uncomment:
    # print(booking_ids)
    # print("The current number of bookings is " + str(len(booking_ids)))
    # print("Datatype before deserialization : "+ str(type(booking_ids)))


# CreateBooking
def test_can_create_booking():
    response_for_create_booking = create_booking()
    # print(response_for_create_booking.json())
    assert response_for_create_booking.status_code == 200
    data = response_for_create_booking.json()
    # print(data)


def test_can_update_booking():
    # create auth token, assign token to a variable
    response_for_create_token = create_token()
    a_token = response_for_create_token.json()['token']

    # create a booking, assign booking id to a variable
    booking_id = get_booking_id()

    # update the created booking using token and booking id
    response_for_update_booking = update_booking(a_token, booking_id)
    assert response_for_update_booking.status_code == 200
    booking = response_for_update_booking.json()

    # verification test: returned updated booking information matches sent data in file restful-booker_API_tests.test_can_update_booking.approved.txt
    result = booking
    verify(result)


def test_can_partial_update_booking():
    # create auth token, assign token to a variable
    response_for_create_token = create_token()
    a_token = response_for_create_token.json()['token']

    # create a booking, assign booking id to a variable
    booking_id = get_booking_id()

    response_for_partial_update_booking = partial_update_booking(a_token, booking_id)
    assert response_for_partial_update_booking.status_code == 200


def test_can_delete_booking():
    # create auth token, assign token to a variable
    response_for_create_token = create_token()
    a_token = response_for_create_token.json()['token']

    # create a booking, assign booking id to variable
    booking_id = get_booking_id()

    # delete the booking
    response_for_delete_booking = delete_booking(a_token, booking_id)
    assert response_for_delete_booking.status_code == 201
    # if response_for_delete_booking.status_code == 201:
    #     print("Booking successfully deleted")
    # else:
    #     print("Deletion failed")

