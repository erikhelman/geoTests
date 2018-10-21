#!/usr/bin/env python3
import requests
import sys
import os

from os.path import sep

# The following two lines add the data folder to the sys.path so the data modules are available
datafilepath = os.getcwd() + sep + 'data'
sys.path.insert(0, datafilepath)


def test_01_geocoding(config_data, data_test_geo_functional):
    """This test retrieves coordinates of a given address from the API with various parameters
    1. Specific address (street number, city, state, zip code, country)
    2. Place name and country
    3. Country only
    4. Address and optional region parameter
    5. Address and optional language parameter
    6. Address and optional component parameter
    7. Components only
    8. Ambiguous search term resulting in multiple results returned
    9. Narrow search results using the optional bounds parameter
    10. Reverse geocoding using latlng
    11. Reverse geocoding using one optional result_type parameter
    12. Reverse geocoding using multiple result_type parameters
    13. Reverse geocoding using location_type parameter
    14: Reverse geocoding using multiple location_type parameters
    15: Reverse geocoding using place id
    """

    api_url = config_data['url'] + config_data['output_format']

    params = data_test_geo_functional[0]
    params['key'] = config_data['api_key']

    resp = requests.get(api_url, params=params)

    assert resp.status_code == 200
    assert resp.json() == data_test_geo_functional[1]

    return resp
