def generate_file_name(origin, destination, departure_date):
    departure_date_str = departure_date.strftime('%Y-%m-%d')
    return f"{origin}-{destination}-{departure_date_str}.json"

def generate_departure_date(self, departureDate = None, days = 14):
    if not departureDate:
        delta = timedelta(days=days)
        departureDate = datetime.today() + delta
    return departureDate