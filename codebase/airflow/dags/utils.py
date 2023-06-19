from datetime import timedelta, datetime

def generate_file_name(origin, destination, departure_date_str):
    date_str = datetime.strptime(departure_date_str, "%Y-%m-%d").strftime("%Y-%m-%d")
    return f"{origin}-{destination}-{date_str}.json"

def generate_departure_date(departureDate = None, days = 14):
    if not departureDate:
        delta = timedelta(days=days)
        departureDate = datetime.today() + delta
    return departureDate