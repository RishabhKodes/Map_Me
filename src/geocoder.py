from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="GCP PROJECT NAME")

def get_coords(address):
    location = geolocator.geocode(address)
    latitude = location.latitude
    longitude = location.longitude
    return f"{latitude},{longitude}"