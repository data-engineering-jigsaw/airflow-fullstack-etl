from datetime import timedelta, datetime

def generate_file_name(origin, destination, departure_date_str):
    
    return f"{origin}-{destination}-{departure_date_str}.json"

def generate_departure_date(departureDate = None, days = 14):
    if not departureDate:
        delta = timedelta(days=days)
        departureDate = datetime.today() + delta
    return departureDate