import requests
import ast
from amadeus import Client, ResponseError, Location
from django.shortcuts import render, redirect
from django.contrib import messages

from demo.booking import Booking



amadeus = Client()

# Step 1: Obtain the access token
def get_access_token():
    try:
        response = requests.post('https://api.amadeus.com/v1/security/oauth2/token', 
            data={
                'grant_type': 'client_credentials',
                'client_id': "MqKAme8vMRNgkipLAHN9JRX9VLotKBom",  # Fetching from environment variables
                'client_secret': "Xg6PsIBzcZ6YyhXW"  # Fetching from environment variables
            })
        response.raise_for_status()  # Check for errors
        token_data = response.json()

        print(token_data['access_token'])
        return token_data['access_token']
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to get access token: {str(e)}")

# Step 2: Update the book_flight view
def book_flight(request, flight):
    token = get_access_token()  # Get the access token from the helper function
    headers = {
        'Authorization': f'Bearer {token}',  # Add the access token in the header
        'Content-Type': 'application/json'
    }

    try:
        # Create a fake traveler profile for booking (you can update this as needed)
        traveler = {
            "id": "1",
            "dateOfBirth": "1982-01-16",
            "name": {"firstName": "JORGE", "lastName": "GONZALES"},
            "gender": "MALE",
            "contact": {
                "emailAddress": "jorge.gonzales833@telefonica.es",
                "phones": [
                    {
                        "deviceType": "MOBILE",
                        "countryCallingCode": "34",
                        "number": "480080076",
                    }
                ],
            },
            "documents": [
                {
                    "documentType": "PASSPORT",
                    "birthPlace": "Madrid",
                    "issuanceLocation": "Madrid",
                    "issuanceDate": "2015-04-14",
                    "number": "00000000",
                    "expiryDate": "2025-04-14",
                    "issuanceCountry": "ES",
                    "validityCountry": "ES",
                    "nationality": "ES",
                    "holder": True,
                }
            ],
        }

        # Step 3: Confirm price and availability of the flight using the Amadeus API
        flight_price_confirmed = amadeus.shopping.flight_offers.pricing.post(
            ast.literal_eval(flight)
        ).data["flightOffers"]

        # Step 4: Send the booking request with the access token
        response = requests.post(
            'https://api.amadeus.com/v1/booking/flight-orders', 
            headers=headers, 
            json={"data": {"type": "flight-order", "flightOffers": flight_price_confirmed, "travelers": [traveler]}}
        )
        response.raise_for_status()  # Check if the request was successful

        # Parse the booking response and render the results page
        order = response.json()["data"]
        passenger_name_record = [Booking(order).construct_booking()]

        return render(request, "demo/book_flight.html", {"response": passenger_name_record})

    except requests.exceptions.HTTPError as http_err:
        messages.error(request, f"Booking failed: {str(http_err)}")
    except (ResponseError, KeyError, AttributeError) as error:
        messages.error(request, f"Booking failed: {str(error)}")

    return render(request, "demo/book_flight.html")
