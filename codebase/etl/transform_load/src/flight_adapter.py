class AmadeusFlightAdapter:
    def __init__(self, flight_json):
        self.json = flight_json

    def segments(self):
        return self.json['itineraries'][0]['segments']

    def select_attributes(self):
        segments = self.segments()
        first_segment = segments[0]
        departure_time = first_segment['departure']['at']
        last_segment = segments[-1]
        arrival_time = last_segment['arrival']['at']
        departure_airport = first_segment['departure']['iataCode']
        arrival_airport = last_segment['arrival']['iataCode']
        total_price = self.json['price']['total']
        
        return {'departure_time': departure_time, 
                'arrival_time': arrival_time, 
                'departure_airport': departure_airport, 
                'arrival_airport': arrival_airport, 'total_price': total_price}