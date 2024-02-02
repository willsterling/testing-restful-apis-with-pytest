import requests
from config import BOOKER_URI

# HELPER FUNCTIONS
# create token

# create authorization (credentials below are required for successful creation of token)
def new_auth():
    return {
        "username": "admin",
        "password": "password123"
    }

def create_token():
    auth = new_auth()
    return requests.post(BOOKER_URI + '/auth', json=auth)
# helper function ; refactor the response for update task

def get_booking_ids():
    return requests.get(BOOKER_URI + '/booking/')

def get_booking(booking_id):
    return requests.get(BOOKER_URI + f'/booking/{booking_id}')

def create_booking():
    data = {
        "firstname": "Jacques",
        "lastname": "Revolt",
        "totalprice": 1200,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-01-01",
            "checkout": "2023-01-10"
        },
        "additionalneeds": "test booking"
    }
    return requests.post(BOOKER_URI + '/booking', json=data)

def update_booking(a_token, booking_id):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Cookie': f'token={a_token}'
    }
    data = {
        "firstname": "Jacob",
        "lastname": "Redford",
        "totalprice": 1350,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-15",
            "checkout": "2024-01-17"
        },
        "additionalneeds": "Breakfast"
    }
    return requests.put(BOOKER_URI + f'/booking/{booking_id}', headers=headers, json=data)

def partial_update_booking(a_token, booking_id):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Cookie': f'token={a_token}'
    }
    data = {
        "firstname": "James",
        "lastname": "Brown",
    }
    return requests.patch(BOOKER_URI + f'/booking/{booking_id}', headers=headers, json=data)

def delete_booking(a_token, booking_id):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Cookie': f'token={a_token}'
    }
    return requests.delete(BOOKER_URI + f'/booking/{booking_id}', headers=headers)