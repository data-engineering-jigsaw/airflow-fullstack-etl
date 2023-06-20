import requests
import json
from requests.structures import CaseInsensitiveDict
from requests.auth import HTTPBasicAuth
from settings import client_id, client_secret
from datetime import datetime, timedelta


class AmadeusClient:
    AUTH_URL = "https://test.api.amadeus.com/v1/security/oauth2/token"
    CLIENT_ID = client_id
    CLIENT_SECRET = client_secret

    def get_access_token(self):
        payload = {'grant_type': 'client_credentials','scope': 'api_agencies_read%20api_listings_read'}
        headers = {"Content-Type" : "application/x-www-form-urlencoded"}
        access_token_response = requests.post(self.AUTH_URL,
                                               auth=HTTPBasicAuth(self.CLIENT_ID, self.CLIENT_SECRET),
                                                 data=payload, headers=headers)
        access_token = access_token_response.json()['access_token']
        return access_token
    
    def search_flights(self, origin, destination, departure_date_str):
        access_token = self.get_access_token()
        headers = CaseInsensitiveDict()
        headers['Authorization'] = f'Bearer {access_token}'
        url = 'https://test.api.amadeus.com/v2/shopping/flight-offers'

        # remove below here 
        departure_date = datetime.strptime(departure_date_str, "%Y-%m-%d").strftime("%Y-%m-%d")
        params = {'originLocationCode': origin,
                'destinationLocationCode': destination,
                'departureDate': departure_date,
                  'adults': str(1)}
        response = requests.get(url, params = params, headers=headers)
        return response.json()

    