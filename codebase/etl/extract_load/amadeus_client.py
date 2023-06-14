import requests
import json
from requests.structures import CaseInsensitiveDict
from requests.auth import HTTPBasicAuth
from etl.extract_load.settings import client_id, client_secret
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
    
    def search_flights(self, origin, destination, departureDate = None):
        access_token = self.get_access_token()
        headers = CaseInsensitiveDict()
        headers['Authorization'] = f'Bearer {access_token}'
        url = 'https://test.api.amadeus.com/v2/shopping/flight-offers'

        departureDate = self.generate_departure_date()
        
        params = {'originLocationCode': origin,
                'destinationLocationCode': destination,
                'departureDate': departureDate.strftime('%Y-%m-%d'), 'adults': str(1)}
        
        response = requests.get(url, params = params, headers=headers)
        return response.json()

    def generate_departure_date(self, departureDate = None, days = 14):
        if not departureDate:
          delta = timedelta(days=days)
          departureDate = datetime.today() + delta
        return departureDate

    def search_and_write(self, origin, destination, departure_date = None):
        departure = self.generate_departure_date(departure_date, days = 14)
        flight_data = self.search_flights(origin, destination, 
                                          departureDate = departure)
        filename = self.generate_file_name(origin, destination, 
                                           departure_date = departure)
        self.write_to_file(flight_data, filename)

    def write_to_file(self, json_data, filename):
        with open(filename, "w") as outfile:
            outfile.write(json.dumps(json_data))

    def generate_file_name(self, origin, destination, departure_date, folder_name = './data'):
        departure_date_str = departure_date.strftime('%Y-%m-%d')
        return f"{folder_name}/{origin}-{destination}-{departure_date_str}.json"