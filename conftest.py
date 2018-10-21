import pytest
import sys
import os
import importlib

from os.path import sep

# The following two lines add the data folder to the sys.path so the data modules are available
datafilepath = os.getcwd() + sep + 'data'
sys.path.insert(0,datafilepath)


@pytest.fixture(scope='session')
def config_data():

    return {"url": "https://maps.googleapis.com/maps/api/geocode",
            "output_format": "/json",
            "api_key": "API_KEY"
            }


def pytest_generate_tests(metafunc):
    """
    This is a hook that exists in pytest that allows test scripts to load data from a module and parameterize
    the data so it can be made available to a test_case
    """

    for fixture in metafunc.fixturenames:
        if fixture.startswith('data_'):
            tests = load_tests(fixture)
            metafunc.parametrize(fixture, tests)


def load_tests(name):
    """
    This is a function that takes in the name of a module and imports it.
    The yield acts like a return but in this case multiple returns of a list of values from the dictionary.
    This is how the test case is able to run multiple times with different data.
    """

    tests_module = importlib.import_module(name)
    for test in tests_module.test_data.values():
        yield test
