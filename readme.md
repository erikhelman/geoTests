# Google Geolocation Test Suite

## About

This suite is a series of tests run using the pytest framework to exercise the Google API Geolocation API. The functional tests are mainly executed via the requests library with a small performance suite demonstration run via jMeter.

The tests require a Google API key. Navigate to the [Google Maps Platform](https://developers.google.com/places/web-service/get-api-key), scroll down and click the button that says "Get A Key" and follow the instructions to acquire a key. The Geocoding API must also be enabled from the developers console.

## Setup

### Prerequisites

This suite and the setup described were created and executed on Ubuntu 18.04 and the project uses Python 3.6.
The latest installation of jMeter is also required.

Install venv (if not already installed)

`sudo apt-get install python3-venv`

Setup a virtual environment to run the project in

`python3 -m venv {folderName}`

cd to the the new folder name and activate the virtual environment

`. bin/activate`

Install the required packages

`pip install -r requirements.txt`

A few configuration changes need to be made before running.

* Edit the conftest.py file and change the parameter set to "API_KEY" to your actual API KEY

* Edit the geo_perf_test.jmx file, search for "API_KEY" and replace it with your actual API KEY

* Edit the run.sh file, change the path to the folder where your jmeter installation is

<pre>
export PATH="$PATH":<b>/home/erik/jmeter/bin</b>
</pre>


### Sphinx configuration 

The project uses Sphinx to generate test case summary documentation. The documentation is uploaded to the repository but to regenrate, follow the steps below

From the command line, type `sphinx-quickstart`

Answer all the questions as below

![Sphinx Setup](sphinx_setup.png)

## Execution

In the root folder, execute the run script
`run.sh`

A folder will be created with the current time stamp that outputs the results from the tests
