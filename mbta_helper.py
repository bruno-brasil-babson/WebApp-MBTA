# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = 'syl6GY2loo9dLvwoCYespfSttcNkeVgq'
MBTA_API_KEY = '4e82acc372e44cd9984f6884fec8798d'
import urllib.request
import urllib.parse
import json
from pprint import pprint

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# A little bit of scaffolding if you want to use it

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    #url = f'http://mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data

# response = get_json(f'http://mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College')
# lat_lng = response['results'][0]['locations'][0]['latLng']
# print(lat_lng)

def get_url(place_name):
    """
    Given a place name or address, return an encoded URL to make the MapQuest request
    """
    edited_place_name = place_name.replace(' ', '%20')
    url = f'http://mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={edited_place_name}'
    return url

def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding API URL formatting requirements.
    """
    url = get_url(place_name)
    geo_data = get_json(url)
    lat_lng = geo_data['results'][0]['locations'][0]['latLng']

    return lat_lng

answer = get_lat_long('Boston Common')
print(answer)

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    url = f'https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)

    return response_data

print(get_nearest_station(33.596, -84.416))


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    pass


def main():
    """
    You can test all the functions here
    """
    pass


if __name__ == '__main__':
    main()
