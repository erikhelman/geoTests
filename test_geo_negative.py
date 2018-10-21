#!/usr/bin/env python3
import requests
import sys
import os
import random
import string

from os.path import sep

# The following two lines add the data folder to the sys.path so the data modules are available
datafilepath = os.getcwd() + sep + 'data'
sys.path.insert(0, datafilepath)


def random_string(length):
    # This function is to generate a random string in some tests below
    return ''.join(random.choice(string.ascii_letters) for i in range(length))


def test_invalid_method_PUT(config_data, data_test_geo_negative):
    """This test attempts to execute the API with an invalid HTTP method - POST"""

    api_url = config_data['url'] + config_data['output_format']

    params = data_test_geo_negative[0]

    params['key'] = config_data['api_key']

    resp = requests.put(api_url, params=params)

    assert resp.status_code == 405
    assert data_test_geo_negative[1] in resp.text

    return resp


def test_invalid_method_DELETE(config_data, data_test_geo_negative):
    """This test attempts to execute the API with an invalid HTTP method - DELETE"""

    api_url = config_data['url'] + config_data['output_format']

    params = data_test_geo_negative[0]
    params['key'] = config_data['api_key']

    resp = requests.delete(api_url, params=params)

    assert resp.status_code == 405
    assert data_test_geo_negative[2] in resp.text

    return resp


def test_url_too_long(config_data, data_test_geo_negative):
    """This test attempts to access the API with a URL that exceeds the allowable length"""

    api_url = config_data['url'] + config_data['output_format']

    params = {"address": random_string(8153),
              "key": config_data['api_key']
              }

    resp = requests.get(api_url, params=params)

    assert resp.status_code == 400
    assert data_test_geo_negative[7] in resp.text

    return resp


def test_invalid_key(config_data, data_test_geo_negative):
    """This test attempts to access the API with an invalid key"""

    api_url = config_data['url'] + config_data['output_format']

    params = data_test_geo_negative[0]
    params['key'] = data_test_geo_negative[3]

    resp = requests.get(api_url, params=params)

    assert resp.status_code == 200
    assert resp.json() == data_test_geo_negative[4]

    return resp


def test_no_key(config_data, data_test_geo_negative):
    """This test attempts to access the API with no API key"""

    api_url = config_data['url'] + config_data['output_format']

    params = data_test_geo_negative[0]
    params['key'] = ""

    resp = requests.get(api_url, params=params)

    assert resp.status_code == 200
    assert resp.json() == data_test_geo_negative[5]

    return resp


def test_no_address(config_data, data_test_geo_negative):
    """This test attempts to access the API with no address parameter"""

    api_url = config_data['url'] + config_data['output_format']

    params = {}
    params['key'] = config_data['api_key']

    resp = requests.get(api_url, params=params)

    assert resp.status_code == 400
    assert resp.json() == data_test_geo_negative[6]

    return resp


def test_invalid_address(config_data, data_test_geo_negative):
    """This test attempts to access the API with a non-existent address"""

    api_url = config_data['url'] + config_data['output_format']

    params = data_test_geo_negative[8]
    params['key'] = config_data['api_key']

    resp = requests.get(api_url, params=params)

    assert resp.status_code == 200
    assert resp.json() == data_test_geo_negative[9]

    return resp


def test_invalid_region(config_data, data_test_geo_negative):
    """This test attempts to access the API with an invalid region"""

    api_url = config_data['url'] + config_data['output_format']

    params = data_test_geo_negative[0]
    params['region'] = data_test_geo_negative[3]
    params['key'] = config_data['api_key']

    resp = requests.get(api_url, params=params)

    assert resp.status_code == 200
    assert resp.json() == data_test_geo_negative[10]

    return resp


def test_invalid_language(config_data, data_test_geo_negative):
    """This test attempts to access the API with an invalid language"""

    api_url = config_data['url'] + config_data['output_format']

    params = data_test_geo_negative[0]
    params['language'] = data_test_geo_negative[3]
    params['key'] = config_data['api_key']

    resp = requests.get(api_url, params=params)

    assert resp.status_code == 200
    assert resp.json() == data_test_geo_negative[10]

    return resp


def test_invalid_components(config_data, data_test_geo_negative):
    """This test attempts to access the API with invalid components"""

    api_url = config_data['url'] + config_data['output_format']

    params = data_test_geo_negative[0]
    params['components'] = data_test_geo_negative[11]
    params['key'] = config_data['api_key']

    resp = requests.get(api_url, params=params)

    assert resp.status_code == 200
    assert resp.json() == data_test_geo_negative[9]

    return resp


def test_no_latlng(config_data, data_test_geo_negative):
    """This test attempts to access the API with no latlng value"""

    api_url = config_data['url'] + config_data['output_format']

    params = data_test_geo_negative[12]
    params['key'] = config_data['api_key']

    resp = requests.get(api_url, params=params)

    assert resp.status_code == 400
    assert resp.json() == data_test_geo_negative[6]

    return resp


def test_invalid_result_type(config_data, data_test_geo_negative):
    """This test attempts to access the API with invalid result type"""

    api_url = config_data['url'] + config_data['output_format']

    params = data_test_geo_negative[15]
    params['result_type'] = data_test_geo_negative[3]
    params['key'] = config_data['api_key']

    resp = requests.get(api_url, params=params)

    assert resp.status_code == 400
    assert resp.json() == data_test_geo_negative[16]

    return resp


def test_invalid_latlng(config_data, data_test_geo_negative):
    """This test attempts to access the API with invalid latlng values"""

    api_url = config_data['url'] + config_data['output_format']

    params = data_test_geo_negative[13]
    params['key'] = config_data['api_key']

    resp = requests.get(api_url, params=params)

    assert resp.status_code == 400
    assert resp.json() == data_test_geo_negative[14]

    return resp


def test_invalid_place_id(config_data, data_test_geo_negative):
    """This test attempts to access the API with an invalid place id"""

    api_url = config_data['url'] + config_data['output_format']

    params = data_test_geo_negative[13]
    params['place_id'] = data_test_geo_negative[3]
    params['key'] = config_data['api_key']

    resp = requests.get(api_url, params=params)

    assert resp.status_code == 400
    assert resp.json() == data_test_geo_negative[18]

    return resp


def test_invalid_location_type(config_data, data_test_geo_negative):
    """This test attempts to access the API with invalid location type"""

    api_url = config_data['url'] + config_data['output_format']

    params = data_test_geo_negative[15]
    params['location_type'] = data_test_geo_negative[3]
    params['key'] = config_data['api_key']

    resp = requests.get(api_url, params=params)

    assert resp.status_code == 400
    assert resp.json() == data_test_geo_negative[17]

    return resp


def test_invalid_bounds(config_data, data_test_geo_negative):
    """This test attempts to access the API with invalid bounds"""

    api_url = config_data['url'] + config_data['output_format']

    params = data_test_geo_negative[0]
    params['bounds'] = data_test_geo_negative[3]
    params['key'] = config_data['api_key']

    resp = requests.get(api_url, params=params)

    assert resp.status_code == 200
    assert resp.json() == data_test_geo_negative[10]

    return resp