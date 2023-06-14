from etl.transform_load.flight_adapter import AmadeusFlightAdapter
import json

class FlightsFileReader:
    def read_from_file(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        return data
    
    def return_flights_from(self, filename):
        flight_json = self.read_from_file(filename)
        flights = flight_json['data']
        selected_flights = []
        
        for flight_json in flights:
            flight_adapter = AmadeusFlightAdapter(flight_json)
            attrs = flight_adapter.select_attributes()
            selected_flights.append(attrs)
        return selected_flights
    
    def write_results_to(self, filename):
        results = self.return_flights_from(filename)
        # write to
