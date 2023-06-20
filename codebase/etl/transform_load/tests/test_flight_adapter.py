import os
from src.flight_adapter import AmadeusFlightAdapter
from tests.data import flights_json

selected_flight = {'type': 'flight-offer', 'id': '12', 'source': 'GDS', 
        'instantTicketingRequired': False, 'nonHomogeneous': False,
        'oneWay': False, 'lastTicketingDate': '2023-06-20',
        'lastTicketingDateTime': '2023-06-20',
        'numberOfBookableSeats': 3, 'itineraries': [{'duration': 'PT7H', 
        'segments': [{'departure': {'iataCode': 'EWR', 'terminal': 'B', 'at': '2023-06-28T10:35:00'},
                       'arrival': {'iataCode': 'ATL', 'terminal': 'S', 'at': '2023-06-28T12:51:00'},
                        'carrierCode': 'DL', 'number': '2198', 'aircraft': {'code': '738'},
                        'operating': {'carrierCode': 'DL'}, 'duration': 'PT2H16M', 'id': '11',
                        'numberOfStops': 0, 'blacklistedInEU': False},
                      {'departure': {'iataCode': 'ATL', 'terminal': 'S', 'at': '2023-06-28T15:43:00'},
                        'arrival': {'iataCode': 'MDW', 'at': '2023-06-28T16:35:00'}, 'carrierCode': 'DL',
                          'number': '2243', 'aircraft': {'code': '320'}, 'operating': {'carrierCode': 'DL'},
                    'duration': 'PT1H52M', 'id': '12', 'numberOfStops': 0, 'blacklistedInEU': False}]}],
                    'price': {'currency': 'EUR', 'total': '156.91', 'base': '125.00',
                    'fees': [{'amount': '0.00', 'type': 'SUPPLIER'},
            {'amount': '0.00', 'type': 'TICKETING'}], 'grandTotal': '156.91'},
                'pricingOptions': {'fareType': ['PUBLISHED'], 'includedCheckedBagsOnly': False},
                'validatingAirlineCodes': ['DL'],
                    'travelerPricings': [{'travelerId': '1', 'fareOption': 'STANDARD', 'travelerType': 'ADULT',
                                           'price': {'currency': 'EUR', 'total': '156.91', 'base': '125.00'}, 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              'fareDetailsBySegment': [{'segmentId': '11', 'cabin': 'ECONOMY', 'fareBasis': 'TA7NA0BC', 'brandedFare': 'BASICECON', 'class': 'E', 'includedCheckedBags': {'quantity': 0}}, {'segmentId': '12', 'cabin': 'ECONOMY', 'fareBasis': 'TA7NA0BC', 'brandedFare': 'BASICECON', 'class': 'E', 'includedCheckedBags': {'quantity': 0}}]}]}

def test_flight_adapter_segments():
    adapter = AmadeusFlightAdapter(selected_flight)
    segments = adapter.segments()
    assert len(segments) == 2
    assert list(segments[0].keys()) == ['departure', 'arrival', 'carrierCode',
                                         'number', 'aircraft', 'operating', 'duration',
                                           'id', 'numberOfStops', 'blacklistedInEU']

def test_flight_adapter_select_attributes():
    adapter = AmadeusFlightAdapter(selected_flight)
    assert adapter.select_attributes() == {'departure_time': '2023-06-28T10:35:00',
                                            'arrival_time': '2023-06-28T16:35:00',
                                              'departure_airport': 'EWR',
                                            'arrival_airport': 'MDW',
                                            'total_price': '156.91'}
