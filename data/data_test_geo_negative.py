test_data = {
    1: (# 0
        {"address": "1600+Amphitheatre+Parkway,+Mountain+View,+CA"},
        # 1
        "The request method <code>PUT</code> is inappropriate for the URL",
        # 2
        "The request method <code>DELETE</code> is inappropriate for the URL",
        # 3
        "INVALID",
        # 4
        {
            "error_message": "The provided API key is invalid.",
            "results": [],
            "status": "REQUEST_DENIED"
        },
        # 5
        {
            "error_message": "Keyless access to Google Maps Platform is deprecated. Please use an API key with all "
                             "your API calls to avoid service interruption. For further details please refer "
                             "to http://g.co/dev/maps-no-account",
            "results": [],
            "status": "OVER_QUERY_LIMIT"
        },
        # 6
        {
            "error_message": "Invalid request. Missing the 'address', 'components', 'latlng' or 'place_id' parameter.",
            "results": [],
            "status": "INVALID_REQUEST"
        },
        # 7
        "Your client has issued a malformed or illegal request.",
        # 8
        {"address": "nonexistentplace"},
        # 9
        {
            "results": [],
            "status": "ZERO_RESULTS"
        },
        # 10
        {
            "results": [
                {
                    "address_components": [
                        {
                            "long_name": "1600",
                            "short_name": "1600",
                            "types": ["street_number"]
                        },
                        {
                            "long_name": "Amphitheatre Parkway",
                            "short_name": "Amphitheatre Pkwy",
                            "types": ["route"]
                        },
                        {
                            "long_name": "Mountain View",
                            "short_name": "Mountain View",
                            "types": ["locality", "political"]
                        },
                        {
                            "long_name": "Santa Clara County",
                            "short_name": "Santa Clara County",
                            "types": ["administrative_area_level_2", "political"]
                        },
                        {
                            "long_name": "California",
                            "short_name": "CA",
                            "types": ["administrative_area_level_1", "political"]
                        },
                        {
                            "long_name": "United States",
                            "short_name": "US",
                            "types": ["country", "political"]
                        },
                        {
                            "long_name": "94043",
                            "short_name": "94043",
                            "types": ["postal_code"]
                        }
                    ],
                    "formatted_address": "1600 Amphitheatre Pkwy, Mountain View, CA 94043, USA",
                    "geometry": {
                        "location": {
                            "lat": 37.4223856,
                            "lng": -122.0858516
                        },
                        "location_type": "ROOFTOP",
                        "viewport": {
                            "northeast": {
                                "lat": 37.42373458029149,
                                "lng": -122.0845026197085
                            },
                            "southwest": {
                                "lat": 37.4210366197085,
                                "lng": -122.0872005802915
                            }
                        }
                    },
                    "place_id": "ChIJ2eUgeAK6j4ARbn5u_wAGqWA",
                    "plus_code": {
                        "compound_code": "CWC7+XM Mountain View, California, United States",
                        "global_code": "849VCWC7+XM"
                    },
                    "types": ["street_address"]
                }
            ],
            "status": "OK"
        },
        # 11
        "country:INVALID",
        # 12
        {"latlng": ""},
        # 13
        {"latlng": "34,-198"},
        # 14
        {
           "error_message" : "Invalid request. Invalid 'latlng' parameter.",
           "results" : [],
           "status" : "INVALID_REQUEST"
        },
        # 15
        {"latlng": "30,90"},
        # 16
        {
           "error_message" : "Invalid request. Invalid 'result_type' parameter.",
           "results" : [],
           "status" : "INVALID_REQUEST"
        },
        # 17
        {
           "error_message" : "Invalid request. Invalid 'location_type' parameter.",
           "results" : [],
           "status" : "INVALID_REQUEST"
        },
        # 18
        {
           "error_message" : "Invalid request. Invalid 'place_id' parameter.",
           "results" : [],
           "status" : "INVALID_REQUEST"
        }
    )
}
