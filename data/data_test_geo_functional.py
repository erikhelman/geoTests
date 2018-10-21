# data (api parameters, expected results)

test_data = {
    1: ({
            "address": "1600+Pennsylvania+Ave+NW,+Washington,+DC+20500,+USA"
        },
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
                            "long_name": "Pennsylvania Avenue Northwest",
                            "short_name": "Pennsylvania Ave NW",
                            "types": ["route"]
                        },
                        {
                            "long_name": "Northwest Washington",
                            "short_name": "Northwest Washington",
                            "types": ["neighborhood", "political"]
                        },
                        {
                            "long_name": "Washington",
                            "short_name": "Washington",
                            "types": ["locality", "political"]
                        },
                        {
                            "long_name": "District of Columbia",
                            "short_name": "DC",
                            "types": ["administrative_area_level_1", "political"]
                        },
                        {
                            "long_name": "United States",
                            "short_name": "US",
                            "types": ["country", "political"]
                        },
                        {
                            "long_name": "20500",
                            "short_name": "20500",
                            "types": ["postal_code"]
                        }
                    ],
                    "formatted_address": "1600 Pennsylvania Ave NW, Washington, DC 20500, USA",
                    "geometry":
                        {
                            "bounds":
                                {
                                    "northeast":
                                        {
                                            "lat": 38.8979044,
                                            "lng": -77.0355124
                                        },
                                    "southwest":
                                        {
                                            "lat": 38.8973063,
                                            "lng": -77.03795749999999
                                        }
                                },
                            "location":
                                {
                                    "lat": 38.8976633,
                                    "lng": -77.03657389999999
                                },
                            "location_type": "ROOFTOP",
                            "viewport":
                                {
                                    "northeast":
                                        {
                                            "lat": 38.8989543302915,
                                            "lng": -77.03538596970849
                                        },
                                    "southwest":
                                        {
                                            "lat": 38.8962563697085,
                                            "lng": -77.03808393029151
                                        }
                                }
                        },
                    "place_id": "ChIJGVtI4by3t4kRr51d_Qm_x58",
                    "types": ["establishment", "point_of_interest", "premise"]
                }
            ],
            "status": "OK"
        }
    ),
    2: ({
            "address": "Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu,+New+Zealand"
        },
        {
            "results":
                [
                    {"address_components":
                        [
                            {
                                "long_name": "Taumatawhakatangihangakoauauotamateapokaiwhenuakitanatahu",
                                "short_name": "Taumatawhakatangihangakoauauotamateapokaiwhenuakitanatahu",
                                "types": ["establishment", "natural_feature"]
                            },
                            {
                                "long_name": "Hawke's Bay",
                                "short_name": "Hawke's Bay",
                                "types": ["administrative_area_level_1", "political"]
                            },
                            {
                                "long_name": "New Zealand",
                                "short_name": "NZ",
                                "types": ["country", "political"]
                            },
                            {
                                "long_name": "4292",
                                "short_name": "4292",
                                "types": ["postal_code"]
                            }
                        ],
                        "formatted_address": "Taumatawhakatangihangakoauauotamateapokaiwhenuakitanatahu, Hawke's Bay 4292, New Zealand",
                        "geometry":
                            {
                                "location":
                                    {
                                        "lat": -40.35, "lng": 176.55
                                    },
                                "location_type": "APPROXIMATE",
                                "viewport":
                                    {
                                        "northeast":
                                            {
                                                "lat": -40.3414959, "lng": 176.5660074
                                            },
                                        "southwest":
                                            {
                                                "lat": -40.358503, "lng": 176.5339926
                                            }
                                    }
                            },
                        "place_id": "ChIJFfiCrdo4Qm0RqPwuOAVtaj8",
                        "types": ["establishment", "natural_feature"]
                    }
                ],
            "status": "OK"
        }
    ),
    3: ({
            "address": "Japan"
        },
        {
            "results": [
                {
                    "address_components": [
                        {
                            "long_name": "Japan",
                            "short_name": "JP",
                            "types": ["country", "political"]
                        }
                    ],
                    "formatted_address": "Japan",
                    "geometry": {
                        "bounds": {
                            "northeast": {
                                "lat": 45.6412626,
                                "lng": 154.0031455
                            },
                            "southwest": {
                                "lat": 20.3585295,
                                "lng": 122.8554688
                            }
                        },
                        "location": {
                            "lat": 36.204824,
                            "lng": 138.252924
                        },
                        "location_type": "APPROXIMATE",
                        "viewport": {
                            "northeast": {
                                "lat": 45.6412626,
                                "lng": 154.0031455
                            },
                            "southwest": {
                                "lat": 20.3585295,
                                "lng": 122.8554688
                            }
                        }
                    },
                    "place_id": "ChIJLxl_1w9OZzQRRFJmfNR1QvU",
                    "types": ["country", "political"]
                }
            ],
            "status": "OK"
        }
    ),
    4: ({
            "address": "munich,+germany",
            "language": "de"
        },
        {
            "results": [
                {
                    "address_components": [
                        {
                            "long_name": "München",
                            "short_name": "München",
                            "types": ["locality", "political"]
                        },
                        {
                            "long_name": "Oberbayern",
                            "short_name": "Oberbayern",
                            "types": ["administrative_area_level_2", "political"]
                        },
                        {
                            "long_name": "Bayern",
                            "short_name": "BY",
                            "types": ["administrative_area_level_1", "political"]
                        },
                        {
                            "long_name": "Deutschland",
                            "short_name": "DE",
                            "types": ["country", "political"]
                        }
                    ],
                    "formatted_address": "München, Deutschland",
                    "geometry": {
                        "bounds": {
                            "northeast": {
                                "lat": 48.2482197,
                                "lng": 11.7228755
                            },
                            "southwest": {
                                "lat": 48.0616018,
                                "lng": 11.360796
                            }
                        },
                        "location": {
                            "lat": 48.1351253,
                            "lng": 11.5819805
                        },
                        "location_type": "APPROXIMATE",
                        "viewport": {
                            "northeast": {
                                "lat": 48.2482197,
                                "lng": 11.7228755
                            },
                            "southwest": {
                                "lat": 48.0616018,
                                "lng": 11.360796
                            }
                        }
                    },
                    "place_id": "ChIJ2V-Mo_l1nkcRfZixfUq4DAE",
                    "types": ["locality", "political"]
                }
            ],
            "status": "OK"
        }
    ),
    5: ({
            "address": "Toledo",
            "region": "es"
        },
        {
            "results": [
                {
                    "address_components": [
                        {
                            "long_name": "Toledo",
                            "short_name": "Toledo",
                            "types": ["locality", "political"]
                        },
                        {
                            "long_name": "Toledo",
                            "short_name": "TO",
                            "types": ["administrative_area_level_2", "political"]
                        },
                        {
                            "long_name": "Castile-La Mancha",
                            "short_name": "CM",
                            "types": ["administrative_area_level_1", "political"]
                        },
                        {
                            "long_name": "Spain",
                            "short_name": "ES",
                            "types": ["country", "political"]
                        }
                    ],
                    "formatted_address": "Toledo, Spain",
                    "geometry": {
                        "bounds": {
                            "northeast": {
                                "lat": 39.88605099999999,
                                "lng": -3.9192423
                            },
                            "southwest": {
                                "lat": 39.8383676,
                                "lng": -4.0796176
                            }
                        },
                        "location": {
                            "lat": 39.8628316,
                            "lng": -4.027323099999999
                        },
                        "location_type": "APPROXIMATE",
                        "viewport": {
                            "northeast": {
                                "lat": 39.88605099999999,
                                "lng": -3.9192423
                            },
                            "southwest": {
                                "lat": 39.8383676,
                                "lng": -4.0796176
                            }
                        }
                    },
                    "place_id": "ChIJ8f21C60Lag0R_q11auhbf8Y",
                    "types": ["locality", "political"]
                }
            ],
            "status": "OK"
        }
    ),
    6: ({
            "address": "london",
            "components": "country:CA"
        },
        {
            "results": [
                {
                    "address_components": [
                        {
                            "long_name": "London",
                            "short_name": "London",
                            "types": ["locality", "political"]
                        },
                        {
                            "long_name": "Middlesex County",
                            "short_name": "Middlesex County",
                            "types": ["administrative_area_level_2", "political"]
                        },
                        {
                            "long_name": "Ontario",
                            "short_name": "ON",
                            "types": ["administrative_area_level_1", "political"]
                        },
                        {
                            "long_name": "Canada",
                            "short_name": "CA",
                            "types": ["country", "political"]
                        }
                    ],
                    "formatted_address": "London, ON, Canada",
                    "geometry": {
                        "bounds": {
                            "northeast": {
                                "lat": 43.073245,
                                "lng": -81.1063879
                            },
                            "southwest": {
                                "lat": 42.824517,
                                "lng": -81.390852
                            }
                        },
                        "location": {
                            "lat": 42.9849233,
                            "lng": -81.2452768
                        },
                        "location_type": "APPROXIMATE",
                        "viewport": {
                            "northeast": {
                                "lat": 43.073245,
                                "lng": -81.1063879
                            },
                            "southwest": {
                                "lat": 42.824517,
                                "lng": -81.390852
                            }
                        }
                    },
                    "place_id": "ChIJC5uNqA7yLogRlWsFmmnXxyg",
                    "types": ["locality", "political"]
                }
            ],
            "status": "OK"
        }
    ),
    7: ({
            "components": "postal_code:90210"
        },
        {
            "results": [
                {
                    "address_components": [
                        {
                            "long_name": "#600",
                            "short_name": "#600",
                            "types": ["subpremise"]
                        },
                        {
                            "long_name": "450",
                            "short_name": "450",
                            "types": ["street_number"]
                        },
                        {
                            "long_name": "North Roxbury Drive",
                            "short_name": "N Roxbury Dr",
                            "types": ["route"]
                        },
                        {
                            "long_name": "Beverly Hills",
                            "short_name": "Beverly Hills",
                            "types": ["locality", "political"]
                        },
                        {
                            "long_name": "Los Angeles County",
                            "short_name": "Los Angeles County",
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
                            "long_name": "90210",
                            "short_name": "90210",
                            "types": ["postal_code"]
                        }
                    ],
                    "formatted_address": "450 N Roxbury Dr #600, Beverly Hills, CA 90210, USA",
                    "geometry": {
                        "location": {
                            "lat": 34.0683231,
                            "lng": -118.4069666
                        },
                        "location_type": "ROOFTOP",
                        "viewport": {
                            "northeast": {
                                "lat": 34.0696720802915,
                                "lng": -118.4056176197085
                            },
                            "southwest": {
                                "lat": 34.0669741197085,
                                "lng": -118.4083155802915
                            }
                        }
                    },
                    "place_id": "ChIJ0X23Lgi8woARbiCgULcWgqQ",
                    "plus_code": {
                        "compound_code": "3H9V+86 Beverly Hills, California, United States",
                        "global_code": "85633H9V+86"
                    },
                    "types": ["establishment", "health", "hospital", "point_of_interest"]
                }
            ],
            "status": "OK"
        }
    ),
    8: ({
            "address": "springfield"
        },
        {
            "results": [
                {
                    "address_components": [
                        {
                            "long_name": "Springfield",
                            "short_name": "Springfield",
                            "types": ["locality", "political"]
                        },
                        {
                            "long_name": "Hampden County",
                            "short_name": "Hampden County",
                            "types": ["administrative_area_level_2", "political"]
                        },
                        {
                            "long_name": "Massachusetts",
                            "short_name": "MA",
                            "types": ["administrative_area_level_1", "political"]
                        },
                        {
                            "long_name": "United States",
                            "short_name": "US",
                            "types": ["country", "political"]
                        }
                    ],
                    "formatted_address": "Springfield, MA, USA",
                    "geometry": {
                        "bounds": {
                            "northeast": {
                                "lat": 42.1620859,
                                "lng": -72.471149
                            },
                            "southwest": {
                                "lat": 42.063595,
                                "lng": -72.6215339
                            }
                        },
                        "location": {
                            "lat": 42.1014831,
                            "lng": -72.589811
                        },
                        "location_type": "APPROXIMATE",
                        "viewport": {
                            "northeast": {
                                "lat": 42.1620859,
                                "lng": -72.471149
                            },
                            "southwest": {
                                "lat": 42.063595,
                                "lng": -72.6215339
                            }
                        }
                    },
                    "place_id": "ChIJH7jkCCzm5okRvaq5QdoIGB0",
                    "types": ["locality", "political"]
                },
                {
                    "address_components": [
                        {
                            "long_name": "Springfield",
                            "short_name": "Springfield",
                            "types": ["locality", "political"]
                        },
                        {
                            "long_name": "Springfield Township",
                            "short_name": "Springfield Township",
                            "types": ["administrative_area_level_3", "political"]
                        },
                        {
                            "long_name": "Greene County",
                            "short_name": "Greene County",
                            "types": ["administrative_area_level_2", "political"]
                        },
                        {
                            "long_name": "Missouri",
                            "short_name": "MO",
                            "types": ["administrative_area_level_1", "political"]
                        },
                        {
                            "long_name": "United States",
                            "short_name": "US",
                            "types": ["country", "political"]
                        }
                    ],
                    "formatted_address": "Springfield, MO, USA",
                    "geometry": {
                        "bounds": {
                            "northeast": {
                                "lat": 37.2708071,
                                "lng": -93.1786431
                            },
                            "southwest": {
                                "lat": 37.0874019,
                                "lng": -93.414006
                            }
                        },
                        "location": {
                            "lat": 37.2089572,
                            "lng": -93.29229889999999
                        },
                        "location_type": "APPROXIMATE",
                        "viewport": {
                            "northeast": {
                                "lat": 37.2708071,
                                "lng": -93.1786431
                            },
                            "southwest": {
                                "lat": 37.0874019,
                                "lng": -93.414006
                            }
                        }
                    },
                    "place_id": "ChIJP5jIRfdiz4cRoA1pHrNs_Ws",
                    "types": ["locality", "political"]
                },
                {
                    "address_components": [
                        {
                            "long_name": "Springfield",
                            "short_name": "Springfield",
                            "types": ["locality", "political"]
                        },
                        {
                            "long_name": "Sangamon County",
                            "short_name": "Sangamon County",
                            "types": ["administrative_area_level_2", "political"]
                        },
                        {
                            "long_name": "Illinois",
                            "short_name": "IL",
                            "types": ["administrative_area_level_1", "political"]
                        },
                        {
                            "long_name": "United States",
                            "short_name": "US",
                            "types": ["country", "political"]
                        }
                    ],
                    "formatted_address": "Springfield, IL, USA",
                    "geometry": {
                        "bounds": {
                            "northeast": {
                                "lat": 39.874049,
                                "lng": -89.5684858
                            },
                            "southwest": {
                                "lat": 39.6536259,
                                "lng": -89.7731769
                            }
                        },
                        "location": {
                            "lat": 39.78172130000001,
                            "lng": -89.6501481
                        },
                        "location_type": "APPROXIMATE",
                        "viewport": {
                            "northeast": {
                                "lat": 39.874049,
                                "lng": -89.5684858
                            },
                            "southwest": {
                                "lat": 39.6536259,
                                "lng": -89.7731769
                            }
                        }
                    },
                    "place_id": "ChIJd9HbJB05dYgRIm2ozO6CLOc",
                    "types": ["locality", "political"]
                }
            ],
            "status": "OK"
        }
    ),
    9: ({
            "address": "springfield",
            "bounds": "39.6536259,-89.7731769|39.874049,-89.5684858"
        },
        {
            "results": [
                {
                    "address_components": [
                        {
                            "long_name": "Springfield",
                            "short_name": "Springfield",
                            "types": ["locality", "political"]
                        },
                        {
                            "long_name": "Sangamon County",
                            "short_name": "Sangamon County",
                            "types": ["administrative_area_level_2", "political"]
                        },
                        {
                            "long_name": "Illinois",
                            "short_name": "IL",
                            "types": ["administrative_area_level_1", "political"]
                        },
                        {
                            "long_name": "United States",
                            "short_name": "US",
                            "types": ["country", "political"]
                        }
                    ],
                    "formatted_address": "Springfield, IL, USA",
                    "geometry": {
                        "bounds": {
                            "northeast": {
                                "lat": 39.874049,
                                "lng": -89.5684858
                            },
                            "southwest": {
                                "lat": 39.6536259,
                                "lng": -89.7731769
                            }
                        },
                        "location": {
                            "lat": 39.78172130000001,
                            "lng": -89.6501481
                        },
                        "location_type": "APPROXIMATE",
                        "viewport": {
                            "northeast": {
                                "lat": 39.874049,
                                "lng": -89.5684858
                            },
                            "southwest": {
                                "lat": 39.6536259,
                                "lng": -89.7731769
                            }
                        }
                    },
                    "place_id": "ChIJd9HbJB05dYgRIm2ozO6CLOc",
                    "types": ["locality", "political"]
                }
            ],
            "status": "OK"
        }
    ),
    10: ({
        "latlng": "43.6534399,-79.38409009999999"
        },
        {
           "plus_code" : {
              "compound_code" : "MJ38+99 Toronto, ON, Canada",
              "global_code" : "87M2MJ38+99"
           },
           "results" : [
              {
                 "address_components" : [
                    {
                       "long_name" : "Toronto City Hall",
                       "short_name" : "Toronto City Hall",
                       "types" : [ "premise" ]
                    },
                    {
                       "long_name" : "100",
                       "short_name" : "100",
                       "types" : [ "street_number" ]
                    },
                    {
                       "long_name" : "Queen Street West",
                       "short_name" : "Queen St W",
                       "types" : [ "route" ]
                    },
                    {
                       "long_name" : "Old Toronto",
                       "short_name" : "Old Toronto",
                       "types" : [ "political", "sublocality", "sublocality_level_1" ]
                    },
                    {
                       "long_name" : "Toronto",
                       "short_name" : "Toronto",
                       "types" : [ "locality", "political" ]
                    },
                    {
                       "long_name" : "Toronto Division",
                       "short_name" : "Toronto Division",
                       "types" : [ "administrative_area_level_2", "political" ]
                    },
                    {
                       "long_name" : "Ontario",
                       "short_name" : "ON",
                       "types" : [ "administrative_area_level_1", "political" ]
                    },
                    {
                       "long_name" : "Canada",
                       "short_name" : "CA",
                       "types" : [ "country", "political" ]
                    },
                    {
                       "long_name" : "M5G 1P5",
                       "short_name" : "M5G 1P5",
                       "types" : [ "postal_code" ]
                    }
                 ],
                 "formatted_address" : "Toronto City Hall, 100 Queen St W, Toronto, ON M5G 1P5, Canada",
                 "geometry" : {
                    "location" : {
                       "lat" : 43.6534399,
                       "lng" : -79.38409
                    },
                    "location_type" : "ROOFTOP",
                    "viewport" : {
                       "northeast" : {
                          "lat" : 43.6547888802915,
                          "lng" : -79.38274101970849
                       },
                       "southwest" : {
                          "lat" : 43.6520909197085,
                          "lng" : -79.38543898029151
                       }
                    }
                 },
                 "place_id" : "ChIJRzw6bsw0K4gR6hyvyL0K5hc",
                 "plus_code" : {
                    "compound_code" : "MJ38+99 Toronto, Ontario, Canada",
                    "global_code" : "87M2MJ38+99"
                 },
                 "types" : [ "establishment", "point_of_interest" ]
              },
              {
                 "address_components" : [
                    {
                       "long_name" : "100",
                       "short_name" : "100",
                       "types" : [ "street_number" ]
                    },
                    {
                       "long_name" : "Queen Street West",
                       "short_name" : "Queen St W",
                       "types" : [ "route" ]
                    },
                    {
                       "long_name" : "Old Toronto",
                       "short_name" : "Old Toronto",
                       "types" : [ "political", "sublocality", "sublocality_level_1" ]
                    },
                    {
                       "long_name" : "Toronto",
                       "short_name" : "Toronto",
                       "types" : [ "locality", "political" ]
                    },
                    {
                       "long_name" : "Toronto Division",
                       "short_name" : "Toronto Division",
                       "types" : [ "administrative_area_level_2", "political" ]
                    },
                    {
                       "long_name" : "Ontario",
                       "short_name" : "ON",
                       "types" : [ "administrative_area_level_1", "political" ]
                    },
                    {
                       "long_name" : "Canada",
                       "short_name" : "CA",
                       "types" : [ "country", "political" ]
                    },
                    {
                       "long_name" : "M5H 2N2",
                       "short_name" : "M5H 2N2",
                       "types" : [ "postal_code" ]
                    }
                 ],
                 "formatted_address" : "100 Queen St W, Toronto, ON M5H 2N2, Canada",
                 "geometry" : {
                    "location" : {
                       "lat" : 43.6534234,
                       "lng" : -79.38408319999999
                    },
                    "location_type" : "ROOFTOP",
                    "viewport" : {
                       "northeast" : {
                          "lat" : 43.6547723802915,
                          "lng" : -79.38273421970848
                       },
                       "southwest" : {
                          "lat" : 43.65207441970851,
                          "lng" : -79.3854321802915
                       }
                    }
                 },
                 "place_id" : "ChIJV1e45Mw0K4gRV_9xFKh-KKw",
                 "plus_code" : {
                    "compound_code" : "MJ38+99 Toronto, Ontario, Canada",
                    "global_code" : "87M2MJ38+99"
                 },
                 "types" : [ "street_address" ]
              },
              {
                 "address_components" : [
                    {
                       "long_name" : "M5G",
                       "short_name" : "M5G",
                       "types" : [ "postal_code", "postal_code_prefix" ]
                    },
                    {
                       "long_name" : "Old Toronto",
                       "short_name" : "Old Toronto",
                       "types" : [ "political", "sublocality", "sublocality_level_1" ]
                    },
                    {
                       "long_name" : "Toronto",
                       "short_name" : "Toronto",
                       "types" : [ "locality", "political" ]
                    },
                    {
                       "long_name" : "Toronto Division",
                       "short_name" : "Toronto Division",
                       "types" : [ "administrative_area_level_2", "political" ]
                    },
                    {
                       "long_name" : "Ontario",
                       "short_name" : "ON",
                       "types" : [ "administrative_area_level_1", "political" ]
                    },
                    {
                       "long_name" : "Canada",
                       "short_name" : "CA",
                       "types" : [ "country", "political" ]
                    }
                 ],
                 "formatted_address" : "Toronto, ON M5G, Canada",
                 "geometry" : {
                    "bounds" : {
                       "northeast" : {
                          "lat" : 43.662463,
                          "lng" : -79.380601
                       },
                       "southwest" : {
                          "lat" : 43.6511301,
                          "lng" : -79.39171899999999
                       }
                    },
                    "location" : {
                       "lat" : 43.6579524,
                       "lng" : -79.3873826
                    },
                    "location_type" : "APPROXIMATE",
                    "viewport" : {
                       "northeast" : {
                          "lat" : 43.662463,
                          "lng" : -79.380601
                       },
                       "southwest" : {
                          "lat" : 43.6511301,
                          "lng" : -79.39171899999999
                       }
                    }
                 },
                 "place_id" : "ChIJQ4yqgck0K4gR1f-j38zDpt0",
                 "types" : [ "postal_code", "postal_code_prefix" ]
              },
              {
                 "address_components" : [
                    {
                       "long_name" : "M5G 1P5",
                       "short_name" : "M5G 1P5",
                       "types" : [ "postal_code" ]
                    },
                    {
                       "long_name" : "Old Toronto",
                       "short_name" : "Old Toronto",
                       "types" : [ "political", "sublocality", "sublocality_level_1" ]
                    },
                    {
                       "long_name" : "Toronto",
                       "short_name" : "Toronto",
                       "types" : [ "locality", "political" ]
                    },
                    {
                       "long_name" : "Toronto Division",
                       "short_name" : "Toronto Division",
                       "types" : [ "administrative_area_level_2", "political" ]
                    },
                    {
                       "long_name" : "Ontario",
                       "short_name" : "ON",
                       "types" : [ "administrative_area_level_1", "political" ]
                    },
                    {
                       "long_name" : "Canada",
                       "short_name" : "CA",
                       "types" : [ "country", "political" ]
                    }
                 ],
                 "formatted_address" : "Toronto, ON M5G 1P5, Canada",
                 "geometry" : {
                    "bounds" : {
                       "northeast" : {
                          "lat" : 43.655414,
                          "lng" : -79.382637
                       },
                       "southwest" : {
                          "lat" : 43.6529724,
                          "lng" : -79.3854559
                       }
                    },
                    "location" : {
                       "lat" : 43.6537348,
                       "lng" : -79.38351179999999
                    },
                    "location_type" : "APPROXIMATE",
                    "viewport" : {
                       "northeast" : {
                          "lat" : 43.6555421802915,
                          "lng" : -79.382637
                       },
                       "southwest" : {
                          "lat" : 43.6528442197085,
                          "lng" : -79.3854559
                       }
                    }
                 },
                 "place_id" : "ChIJCb-yics0K4gRL2nyz4fPHN8",
                 "types" : [ "postal_code" ]
              },
              {
                 "address_components" : [
                    {
                       "long_name" : "Downtown",
                       "short_name" : "Downtown",
                       "types" : [ "neighborhood", "political" ]
                    },
                    {
                       "long_name" : "Old Toronto",
                       "short_name" : "Old Toronto",
                       "types" : [ "political", "sublocality", "sublocality_level_1" ]
                    },
                    {
                       "long_name" : "Toronto",
                       "short_name" : "Toronto",
                       "types" : [ "locality", "political" ]
                    },
                    {
                       "long_name" : "Toronto Division",
                       "short_name" : "Toronto Division",
                       "types" : [ "administrative_area_level_2", "political" ]
                    },
                    {
                       "long_name" : "Ontario",
                       "short_name" : "ON",
                       "types" : [ "administrative_area_level_1", "political" ]
                    },
                    {
                       "long_name" : "Canada",
                       "short_name" : "CA",
                       "types" : [ "country", "political" ]
                    }
                 ],
                 "formatted_address" : "Downtown, Toronto, ON, Canada",
                 "geometry" : {
                    "bounds" : {
                       "northeast" : {
                          "lat" : 43.6755833,
                          "lng" : -79.3470176
                       },
                       "southwest" : {
                          "lat" : 43.6339328,
                          "lng" : -79.41131710000001
                       }
                    },
                    "location" : {
                       "lat" : 43.654262,
                       "lng" : -79.385975
                    },
                    "location_type" : "APPROXIMATE",
                    "viewport" : {
                       "northeast" : {
                          "lat" : 43.6755833,
                          "lng" : -79.3470176
                       },
                       "southwest" : {
                          "lat" : 43.6339328,
                          "lng" : -79.41131710000001
                       }
                    }
                 },
                 "place_id" : "ChIJvRBz0jTL1IkRkwMHIgbSFbo",
                 "types" : [ "neighborhood", "political" ]
              },
              {
                 "address_components" : [
                    {
                       "long_name" : "Old Toronto",
                       "short_name" : "Old Toronto",
                       "types" : [ "political", "sublocality", "sublocality_level_1" ]
                    },
                    {
                       "long_name" : "Toronto",
                       "short_name" : "Toronto",
                       "types" : [ "locality", "political" ]
                    },
                    {
                       "long_name" : "Toronto Division",
                       "short_name" : "Toronto Division",
                       "types" : [ "administrative_area_level_2", "political" ]
                    },
                    {
                       "long_name" : "Ontario",
                       "short_name" : "ON",
                       "types" : [ "administrative_area_level_1", "political" ]
                    },
                    {
                       "long_name" : "Canada",
                       "short_name" : "CA",
                       "types" : [ "country", "political" ]
                    }
                 ],
                 "formatted_address" : "Old Toronto, Toronto, ON, Canada",
                 "geometry" : {
                    "bounds" : {
                       "northeast" : {
                          "lat" : 43.75373099999999,
                          "lng" : -79.27971699999999
                       },
                       "southwest" : {
                          "lat" : 43.6118399,
                          "lng" : -79.491969
                       }
                    },
                    "location" : {
                       "lat" : 43.6486795,
                       "lng" : -79.3803231
                    },
                    "location_type" : "APPROXIMATE",
                    "viewport" : {
                       "northeast" : {
                          "lat" : 43.75373099999999,
                          "lng" : -79.27971699999999
                       },
                       "southwest" : {
                          "lat" : 43.6118399,
                          "lng" : -79.491969
                       }
                    }
                 },
                 "place_id" : "ChIJ2YVS1Po0K4gR8_c5_bvmDW4",
                 "types" : [ "political", "sublocality", "sublocality_level_1" ]
              },
              {
                 "address_components" : [
                    {
                       "long_name" : "Toronto",
                       "short_name" : "Toronto",
                       "types" : [ "locality", "political" ]
                    },
                    {
                       "long_name" : "Toronto Division",
                       "short_name" : "Toronto Division",
                       "types" : [ "administrative_area_level_2", "political" ]
                    },
                    {
                       "long_name" : "Ontario",
                       "short_name" : "ON",
                       "types" : [ "administrative_area_level_1", "political" ]
                    },
                    {
                       "long_name" : "Canada",
                       "short_name" : "CA",
                       "types" : [ "country", "political" ]
                    }
                 ],
                 "formatted_address" : "Toronto, ON, Canada",
                 "geometry" : {
                    "bounds" : {
                       "northeast" : {
                          "lat" : 43.8554579,
                          "lng" : -79.00248100000002
                       },
                       "southwest" : {
                          "lat" : 43.45829699999999,
                          "lng" : -79.639219
                       }
                    },
                    "location" : {
                       "lat" : 43.653226,
                       "lng" : -79.3831843
                    },
                    "location_type" : "APPROXIMATE",
                    "viewport" : {
                       "northeast" : {
                          "lat" : 43.8554579,
                          "lng" : -79.00248100000002
                       },
                       "southwest" : {
                          "lat" : 43.45829699999999,
                          "lng" : -79.639219
                       }
                    }
                 },
                 "place_id" : "ChIJpTvG15DL1IkRd8S0KlBVNTI",
                 "types" : [ "locality", "political" ]
              },
              {
                 "address_components" : [
                    {
                       "long_name" : "Toronto Division",
                       "short_name" : "Toronto Division",
                       "types" : [ "administrative_area_level_2", "political" ]
                    },
                    {
                       "long_name" : "Toronto",
                       "short_name" : "Toronto",
                       "types" : [ "locality", "political" ]
                    },
                    {
                       "long_name" : "Ontario",
                       "short_name" : "ON",
                       "types" : [ "administrative_area_level_1", "political" ]
                    },
                    {
                       "long_name" : "Canada",
                       "short_name" : "CA",
                       "types" : [ "country", "political" ]
                    }
                 ],
                 "formatted_address" : "Toronto Division, Toronto, ON, Canada",
                 "geometry" : {
                    "bounds" : {
                       "northeast" : {
                          "lat" : 43.8554579,
                          "lng" : -79.00248100000002
                       },
                       "southwest" : {
                          "lat" : 43.45829699999999,
                          "lng" : -79.639219
                       }
                    },
                    "location" : {
                       "lat" : 43.6689775,
                       "lng" : -79.29021329999999
                    },
                    "location_type" : "APPROXIMATE",
                    "viewport" : {
                       "northeast" : {
                          "lat" : 43.8554579,
                          "lng" : -79.00248100000002
                       },
                       "southwest" : {
                          "lat" : 43.45829699999999,
                          "lng" : -79.639219
                       }
                    }
                 },
                 "place_id" : "ChIJ5b2RG4_L1IkRDtQ2gFEjLv4",
                 "types" : [ "administrative_area_level_2", "political" ]
              },
              {
                 "address_components" : [
                    {
                       "long_name" : "Ontario",
                       "short_name" : "ON",
                       "types" : [ "administrative_area_level_1", "political" ]
                    },
                    {
                       "long_name" : "Canada",
                       "short_name" : "CA",
                       "types" : [ "country", "political" ]
                    }
                 ],
                 "formatted_address" : "Ontario, Canada",
                 "geometry" : {
                    "bounds" : {
                       "northeast" : {
                          "lat" : 56.931393,
                          "lng" : -74.3206479
                       },
                       "southwest" : {
                          "lat" : 41.6765559,
                          "lng" : -95.1562271
                       }
                    },
                    "location" : {
                       "lat" : 51.253775,
                       "lng" : -85.32321399999999
                    },
                    "location_type" : "APPROXIMATE",
                    "viewport" : {
                       "northeast" : {
                          "lat" : 56.931393,
                          "lng" : -74.3206479
                       },
                       "southwest" : {
                          "lat" : 41.6765559,
                          "lng" : -95.1562271
                       }
                    }
                 },
                 "place_id" : "ChIJrxNRX7IFzkwRCR5iKVZC-HA",
                 "types" : [ "administrative_area_level_1", "political" ]
              },
              {
                 "address_components" : [
                    {
                       "long_name" : "Canada",
                       "short_name" : "CA",
                       "types" : [ "country", "political" ]
                    }
                 ],
                 "formatted_address" : "Canada",
                 "geometry" : {
                    "bounds" : {
                       "northeast" : {
                          "lat" : 83.63809999999999,
                          "lng" : -50.9766
                       },
                       "southwest" : {
                          "lat" : 41.6765559,
                          "lng" : -141.00187
                       }
                    },
                    "location" : {
                       "lat" : 56.130366,
                       "lng" : -106.346771
                    },
                    "location_type" : "APPROXIMATE",
                    "viewport" : {
                       "northeast" : {
                          "lat" : 83.63809999999999,
                          "lng" : -50.9766
                       },
                       "southwest" : {
                          "lat" : 41.6765559,
                          "lng" : -141.00187
                       }
                    }
                 },
                 "place_id" : "ChIJ2WrMN9MDDUsRpY9Doiq3aJk",
                 "types" : [ "country", "political" ]
              }
           ],
           "status" : "OK"
        }
    ),
    11: ({
        "latlng": "43.6534399,-79.38409009999999",
        "result_type": "street_address"
        },
        {
           "plus_code" : {
              "compound_code" : "MJ38+99 Toronto, ON, Canada",
              "global_code" : "87M2MJ38+99"
           },
           "results" : [
              {
                 "address_components" : [
                    {
                       "long_name" : "100",
                       "short_name" : "100",
                       "types" : [ "street_number" ]
                    },
                    {
                       "long_name" : "Queen Street West",
                       "short_name" : "Queen St W",
                       "types" : [ "route" ]
                    },
                    {
                       "long_name" : "Old Toronto",
                       "short_name" : "Old Toronto",
                       "types" : [ "political", "sublocality", "sublocality_level_1" ]
                    },
                    {
                       "long_name" : "Toronto",
                       "short_name" : "Toronto",
                       "types" : [ "locality", "political" ]
                    },
                    {
                       "long_name" : "Toronto Division",
                       "short_name" : "Toronto Division",
                       "types" : [ "administrative_area_level_2", "political" ]
                    },
                    {
                       "long_name" : "Ontario",
                       "short_name" : "ON",
                       "types" : [ "administrative_area_level_1", "political" ]
                    },
                    {
                       "long_name" : "Canada",
                       "short_name" : "CA",
                       "types" : [ "country", "political" ]
                    },
                    {
                       "long_name" : "M5H 2N2",
                       "short_name" : "M5H 2N2",
                       "types" : [ "postal_code" ]
                    }
                 ],
                 "formatted_address" : "100 Queen St W, Toronto, ON M5H 2N2, Canada",
                 "geometry" : {
                    "location" : {
                       "lat" : 43.6534234,
                       "lng" : -79.38408319999999
                    },
                    "location_type" : "ROOFTOP",
                    "viewport" : {
                       "northeast" : {
                          "lat" : 43.6547723802915,
                          "lng" : -79.38273421970848
                       },
                       "southwest" : {
                          "lat" : 43.65207441970851,
                          "lng" : -79.3854321802915
                       }
                    }
                 },
                 "place_id" : "ChIJV1e45Mw0K4gRV_9xFKh-KKw",
                 "plus_code" : {
                    "compound_code" : "MJ38+99 Toronto, Ontario, Canada",
                    "global_code" : "87M2MJ38+99"
                 },
                 "types" : [ "street_address" ]
              }
           ],
           "status" : "OK"
        }
    ),
    12: ({
        "latlng": "41.8902102,12.4922309",
        "result_type": "bus_station|transit_station"
        },
        {
           "plus_code" : {
              "compound_code" : "VFRR+3V Rome, Metropolitan City of Rome, Italy",
              "global_code" : "8FHJVFRR+3V"
           },
           "results" : [
              {
                 "address_components" : [
                    {
                       "long_name" : "Celio Vibenna",
                       "short_name" : "Celio Vibenna",
                       "types" : [
                          "bus_station",
                          "establishment",
                          "point_of_interest",
                          "transit_station"
                       ]
                    },
                    {
                       "long_name" : "Roma",
                       "short_name" : "Roma",
                       "types" : [ "locality", "political" ]
                    },
                    {
                       "long_name" : "Roma",
                       "short_name" : "Roma",
                       "types" : [ "administrative_area_level_3", "political" ]
                    },
                    {
                       "long_name" : "Città Metropolitana di Roma",
                       "short_name" : "RM",
                       "types" : [ "administrative_area_level_2", "political" ]
                    },
                    {
                       "long_name" : "Lazio",
                       "short_name" : "Lazio",
                       "types" : [ "administrative_area_level_1", "political" ]
                    },
                    {
                       "long_name" : "Italy",
                       "short_name" : "IT",
                       "types" : [ "country", "political" ]
                    },
                    {
                       "long_name" : "00184",
                       "short_name" : "00184",
                       "types" : [ "postal_code" ]
                    }
                 ],
                 "formatted_address" : "Celio Vibenna, 00184 Roma RM, Italy",
                 "geometry" : {
                    "location" : {
                       "lat" : 41.8893276,
                       "lng" : 12.4927727
                    },
                    "location_type" : "GEOMETRIC_CENTER",
                    "viewport" : {
                       "northeast" : {
                          "lat" : 41.8906765802915,
                          "lng" : 12.4941216802915
                       },
                       "southwest" : {
                          "lat" : 41.8879786197085,
                          "lng" : 12.4914237197085
                       }
                    }
                 },
                 "place_id" : "ChIJSZa0rbdhLxMRVYJICH1eyk8",
                 "plus_code" : {
                    "compound_code" : "VFQV+P4 Rome, Metropolitan City of Rome, Italy",
                    "global_code" : "8FHJVFQV+P4"
                 },
                 "types" : [
                    "bus_station",
                    "establishment",
                    "point_of_interest",
                    "transit_station"
                 ]
              }
           ],
           "status" : "OK"
        }
    ),
    13: ({
        "latlng": "44.3668152,-79.66412900000002",
        "location_type": "ROOFTOP"
        },
        {
           "plus_code" : {
              "compound_code" : "988P+P8 Barrie, ON, Canada",
              "global_code" : "87P2988P+P8"
           },
           "results" : [
              {
                 "address_components" : [
                    {
                       "long_name" : "#3",
                       "short_name" : "#3",
                       "types" : [ "subpremise" ]
                    },
                    {
                       "long_name" : "384",
                       "short_name" : "384",
                       "types" : [ "street_number" ]
                    },
                    {
                       "long_name" : "Yonge Street",
                       "short_name" : "Yonge St",
                       "types" : [ "route" ]
                    },
                    {
                       "long_name" : "Barrie",
                       "short_name" : "Barrie",
                       "types" : [ "locality", "political" ]
                    },
                    {
                       "long_name" : "Simcoe County",
                       "short_name" : "Simcoe County",
                       "types" : [ "administrative_area_level_2", "political" ]
                    },
                    {
                       "long_name" : "Ontario",
                       "short_name" : "ON",
                       "types" : [ "administrative_area_level_1", "political" ]
                    },
                    {
                       "long_name" : "Canada",
                       "short_name" : "CA",
                       "types" : [ "country", "political" ]
                    },
                    {
                       "long_name" : "L4N 4C8",
                       "short_name" : "L4N 4C8",
                       "types" : [ "postal_code" ]
                    }
                 ],
                 "formatted_address" : "384 Yonge St #3, Barrie, ON L4N 4C8, Canada",
                 "geometry" : {
                    "location" : {
                       "lat" : 44.3668152,
                       "lng" : -79.66412900000002
                    },
                    "location_type" : "ROOFTOP",
                    "viewport" : {
                       "northeast" : {
                          "lat" : 44.36816418029149,
                          "lng" : -79.66278001970852
                       },
                       "southwest" : {
                          "lat" : 44.3654662197085,
                          "lng" : -79.66547798029153
                       }
                    }
                 },
                 "place_id" : "ChIJk1BblLy8KogRqAYkVyr-Oek",
                 "plus_code" : {
                    "compound_code" : "988P+P8 Barrie, Ontario, Canada",
                    "global_code" : "87P2988P+P8"
                 },
                 "types" : [
                    "bar",
                    "establishment",
                    "food",
                    "liquor_store",
                    "point_of_interest",
                    "restaurant",
                    "store"
                 ]
              },
              {
                 "address_components" : [
                    {
                       "long_name" : "384",
                       "short_name" : "384",
                       "types" : [ "street_number" ]
                    },
                    {
                       "long_name" : "Yonge Street",
                       "short_name" : "Yonge St",
                       "types" : [ "route" ]
                    },
                    {
                       "long_name" : "Barrie",
                       "short_name" : "Barrie",
                       "types" : [ "locality", "political" ]
                    },
                    {
                       "long_name" : "Simcoe County",
                       "short_name" : "Simcoe County",
                       "types" : [ "administrative_area_level_2", "political" ]
                    },
                    {
                       "long_name" : "Ontario",
                       "short_name" : "ON",
                       "types" : [ "administrative_area_level_1", "political" ]
                    },
                    {
                       "long_name" : "Canada",
                       "short_name" : "CA",
                       "types" : [ "country", "political" ]
                    },
                    {
                       "long_name" : "L4N 4C8",
                       "short_name" : "L4N 4C8",
                       "types" : [ "postal_code" ]
                    }
                 ],
                 "formatted_address" : "384 Yonge St, Barrie, ON L4N 4C8, Canada",
                 "geometry" : {
                    "location" : {
                       "lat" : 44.3667689,
                       "lng" : -79.66398099999999
                    },
                    "location_type" : "ROOFTOP",
                    "viewport" : {
                       "northeast" : {
                          "lat" : 44.36811788029151,
                          "lng" : -79.6626320197085
                       },
                       "southwest" : {
                          "lat" : 44.36541991970851,
                          "lng" : -79.6653299802915
                       }
                    }
                 },
                 "place_id" : "ChIJ3xnViby8KogR2namzov3dyU",
                 "plus_code" : {
                    "compound_code" : "988P+PC Barrie, Ontario, Canada",
                    "global_code" : "87P2988P+PC"
                 },
                 "types" : [ "street_address" ]
              }
           ],
           "status" : "OK"
        }
    ),
    14: ({
             "latlng": "44.3668152,-79.66412900000002",
             "location_type": "ROOFTOP|APPROXIMATE"
        },
        {
           "plus_code" : {
              "compound_code" : "988P+P8 Barrie, ON, Canada",
              "global_code" : "87P2988P+P8"
           },
           "results" : [
              {
                 "address_components" : [
                    {
                       "long_name" : "#3",
                       "short_name" : "#3",
                       "types" : [ "subpremise" ]
                    },
                    {
                       "long_name" : "384",
                       "short_name" : "384",
                       "types" : [ "street_number" ]
                    },
                    {
                       "long_name" : "Yonge Street",
                       "short_name" : "Yonge St",
                       "types" : [ "route" ]
                    },
                    {
                       "long_name" : "Barrie",
                       "short_name" : "Barrie",
                       "types" : [ "locality", "political" ]
                    },
                    {
                       "long_name" : "Simcoe County",
                       "short_name" : "Simcoe County",
                       "types" : [ "administrative_area_level_2", "political" ]
                    },
                    {
                       "long_name" : "Ontario",
                       "short_name" : "ON",
                       "types" : [ "administrative_area_level_1", "political" ]
                    },
                    {
                       "long_name" : "Canada",
                       "short_name" : "CA",
                       "types" : [ "country", "political" ]
                    },
                    {
                       "long_name" : "L4N 4C8",
                       "short_name" : "L4N 4C8",
                       "types" : [ "postal_code" ]
                    }
                 ],
                 "formatted_address" : "384 Yonge St #3, Barrie, ON L4N 4C8, Canada",
                 "geometry" : {
                    "location" : {
                       "lat" : 44.3668152,
                       "lng" : -79.66412900000002
                    },
                    "location_type" : "ROOFTOP",
                    "viewport" : {
                       "northeast" : {
                          "lat" : 44.36816418029149,
                          "lng" : -79.66278001970852
                       },
                       "southwest" : {
                          "lat" : 44.3654662197085,
                          "lng" : -79.66547798029153
                       }
                    }
                 },
                 "place_id" : "ChIJk1BblLy8KogRqAYkVyr-Oek",
                 "plus_code" : {
                    "compound_code" : "988P+P8 Barrie, Ontario, Canada",
                    "global_code" : "87P2988P+P8"
                 },
                 "types" : [
                    "bar",
                    "establishment",
                    "food",
                    "liquor_store",
                    "point_of_interest",
                    "restaurant",
                    "store"
                 ]
              },
              {
                 "address_components" : [
                    {
                       "long_name" : "384",
                       "short_name" : "384",
                       "types" : [ "street_number" ]
                    },
                    {
                       "long_name" : "Yonge Street",
                       "short_name" : "Yonge St",
                       "types" : [ "route" ]
                    },
                    {
                       "long_name" : "Barrie",
                       "short_name" : "Barrie",
                       "types" : [ "locality", "political" ]
                    },
                    {
                       "long_name" : "Simcoe County",
                       "short_name" : "Simcoe County",
                       "types" : [ "administrative_area_level_2", "political" ]
                    },
                    {
                       "long_name" : "Ontario",
                       "short_name" : "ON",
                       "types" : [ "administrative_area_level_1", "political" ]
                    },
                    {
                       "long_name" : "Canada",
                       "short_name" : "CA",
                       "types" : [ "country", "political" ]
                    },
                    {
                       "long_name" : "L4N 4C8",
                       "short_name" : "L4N 4C8",
                       "types" : [ "postal_code" ]
                    }
                 ],
                 "formatted_address" : "384 Yonge St, Barrie, ON L4N 4C8, Canada",
                 "geometry" : {
                    "location" : {
                       "lat" : 44.3667689,
                       "lng" : -79.66398099999999
                    },
                    "location_type" : "ROOFTOP",
                    "viewport" : {
                       "northeast" : {
                          "lat" : 44.36811788029151,
                          "lng" : -79.6626320197085
                       },
                       "southwest" : {
                          "lat" : 44.36541991970851,
                          "lng" : -79.6653299802915
                       }
                    }
                 },
                 "place_id" : "ChIJ3xnViby8KogR2namzov3dyU",
                 "plus_code" : {
                    "compound_code" : "988P+PC Barrie, Ontario, Canada",
                    "global_code" : "87P2988P+PC"
                 },
                 "types" : [ "street_address" ]
              },
              {
                 "address_components" : [
                    {
                       "long_name" : "L4N 2Z6",
                       "short_name" : "L4N 2Z6",
                       "types" : [ "postal_code" ]
                    },
                    {
                       "long_name" : "Barrie",
                       "short_name" : "Barrie",
                       "types" : [ "locality", "political" ]
                    },
                    {
                       "long_name" : "Simcoe County",
                       "short_name" : "Simcoe County",
                       "types" : [ "administrative_area_level_2", "political" ]
                    },
                    {
                       "long_name" : "Ontario",
                       "short_name" : "ON",
                       "types" : [ "administrative_area_level_1", "political" ]
                    },
                    {
                       "long_name" : "Canada",
                       "short_name" : "CA",
                       "types" : [ "country", "political" ]
                    }
                 ],
                 "formatted_address" : "Barrie, ON L4N 2Z6, Canada",
                 "geometry" : {
                    "bounds" : {
                       "northeast" : {
                          "lat" : 44.3674105,
                          "lng" : -79.66232169999999
                       },
                       "southwest" : {
                          "lat" : 44.36533499999999,
                          "lng" : -79.6687204
                       }
                    },
                    "location" : {
                       "lat" : 44.3665873,
                       "lng" : -79.6659981
                    },
                    "location_type" : "APPROXIMATE",
                    "viewport" : {
                       "northeast" : {
                          "lat" : 44.36772173029149,
                          "lng" : -79.66232169999999
                       },
                       "southwest" : {
                          "lat" : 44.3650237697085,
                          "lng" : -79.6687204
                       }
                    }
                 },
                 "place_id" : "ChIJX3FDOby8KogR1CS2XPGXFJo",
                 "types" : [ "postal_code" ]
              },
              {
                 "address_components" : [
                    {
                       "long_name" : "L4N",
                       "short_name" : "L4N",
                       "types" : [ "postal_code", "postal_code_prefix" ]
                    },
                    {
                       "long_name" : "Barrie",
                       "short_name" : "Barrie",
                       "types" : [ "locality", "political" ]
                    },
                    {
                       "long_name" : "Simcoe County",
                       "short_name" : "Simcoe County",
                       "types" : [ "administrative_area_level_2", "political" ]
                    },
                    {
                       "long_name" : "Ontario",
                       "short_name" : "ON",
                       "types" : [ "administrative_area_level_1", "political" ]
                    },
                    {
                       "long_name" : "Canada",
                       "short_name" : "CA",
                       "types" : [ "country", "political" ]
                    }
                 ],
                 "formatted_address" : "Barrie, ON L4N, Canada",
                 "geometry" : {
                    "bounds" : {
                       "northeast" : {
                          "lat" : 44.422491,
                          "lng" : -79.61113109999999
                       },
                       "southwest" : {
                          "lat" : 44.3157529,
                          "lng" : -79.7807919
                       }
                    },
                    "location" : {
                       "lat" : 44.3680579,
                       "lng" : -79.7175517
                    },
                    "location_type" : "APPROXIMATE",
                    "viewport" : {
                       "northeast" : {
                          "lat" : 44.422491,
                          "lng" : -79.61113109999999
                       },
                       "southwest" : {
                          "lat" : 44.3157529,
                          "lng" : -79.7807919
                       }
                    }
                 },
                 "place_id" : "ChIJoW8s9x-9KogRQx5kjgePvy4",
                 "types" : [ "postal_code", "postal_code_prefix" ]
              },
              {
                 "address_components" : [
                    {
                       "long_name" : "Barrie",
                       "short_name" : "Barrie",
                       "types" : [ "locality", "political" ]
                    },
                    {
                       "long_name" : "Simcoe County",
                       "short_name" : "Simcoe County",
                       "types" : [ "administrative_area_level_2", "political" ]
                    },
                    {
                       "long_name" : "Ontario",
                       "short_name" : "ON",
                       "types" : [ "administrative_area_level_1", "political" ]
                    },
                    {
                       "long_name" : "Canada",
                       "short_name" : "CA",
                       "types" : [ "country", "political" ]
                    }
                 ],
                 "formatted_address" : "Barrie, ON, Canada",
                 "geometry" : {
                    "bounds" : {
                       "northeast" : {
                          "lat" : 44.424403,
                          "lng" : -79.5858192
                       },
                       "southwest" : {
                          "lat" : 44.2938755,
                          "lng" : -79.7456249
                       }
                    },
                    "location" : {
                       "lat" : 44.38935559999999,
                       "lng" : -79.69033159999999
                    },
                    "location_type" : "APPROXIMATE",
                    "viewport" : {
                       "northeast" : {
                          "lat" : 44.424403,
                          "lng" : -79.5858192
                       },
                       "southwest" : {
                          "lat" : 44.2938755,
                          "lng" : -79.7456249
                       }
                    }
                 },
                 "place_id" : "ChIJbSDXGjejKogRWlNLqAAPLh0",
                 "types" : [ "locality", "political" ]
              },
              {
                 "address_components" : [
                    {
                       "long_name" : "Simcoe County",
                       "short_name" : "Simcoe County",
                       "types" : [ "administrative_area_level_2", "political" ]
                    },
                    {
                       "long_name" : "Ontario",
                       "short_name" : "ON",
                       "types" : [ "administrative_area_level_1", "political" ]
                    },
                    {
                       "long_name" : "Canada",
                       "short_name" : "CA",
                       "types" : [ "country", "political" ]
                    }
                 ],
                 "formatted_address" : "Simcoe County, ON, Canada",
                 "geometry" : {
                    "bounds" : {
                       "northeast" : {
                          "lat" : 44.98562279999999,
                          "lng" : -79.081878
                       },
                       "southwest" : {
                          "lat" : 43.951448,
                          "lng" : -80.437333
                       }
                    },
                    "location" : {
                       "lat" : 44.4716525,
                       "lng" : -79.82967429999999
                    },
                    "location_type" : "APPROXIMATE",
                    "viewport" : {
                       "northeast" : {
                          "lat" : 44.98562279999999,
                          "lng" : -79.081878
                       },
                       "southwest" : {
                          "lat" : 43.951448,
                          "lng" : -80.437333
                       }
                    }
                 },
                 "place_id" : "ChIJtbFIMeQ61UwRiT6qJMoCDbs",
                 "types" : [ "administrative_area_level_2", "political" ]
              },
              {
                 "address_components" : [
                    {
                       "long_name" : "Ontario",
                       "short_name" : "ON",
                       "types" : [ "administrative_area_level_1", "political" ]
                    },
                    {
                       "long_name" : "Canada",
                       "short_name" : "CA",
                       "types" : [ "country", "political" ]
                    }
                 ],
                 "formatted_address" : "Ontario, Canada",
                 "geometry" : {
                    "bounds" : {
                       "northeast" : {
                          "lat" : 56.931393,
                          "lng" : -74.3206479
                       },
                       "southwest" : {
                          "lat" : 41.6765559,
                          "lng" : -95.1562271
                       }
                    },
                    "location" : {
                       "lat" : 51.253775,
                       "lng" : -85.32321399999999
                    },
                    "location_type" : "APPROXIMATE",
                    "viewport" : {
                       "northeast" : {
                          "lat" : 56.931393,
                          "lng" : -74.3206479
                       },
                       "southwest" : {
                          "lat" : 41.6765559,
                          "lng" : -95.1562271
                       }
                    }
                 },
                 "place_id" : "ChIJrxNRX7IFzkwRCR5iKVZC-HA",
                 "types" : [ "administrative_area_level_1", "political" ]
              },
              {
                 "address_components" : [
                    {
                       "long_name" : "Canada",
                       "short_name" : "CA",
                       "types" : [ "country", "political" ]
                    }
                 ],
                 "formatted_address" : "Canada",
                 "geometry" : {
                    "bounds" : {
                       "northeast" : {
                          "lat" : 83.63809999999999,
                          "lng" : -50.9766
                       },
                       "southwest" : {
                          "lat" : 41.6765559,
                          "lng" : -141.00187
                       }
                    },
                    "location" : {
                       "lat" : 56.130366,
                       "lng" : -106.346771
                    },
                    "location_type" : "APPROXIMATE",
                    "viewport" : {
                       "northeast" : {
                          "lat" : 83.63809999999999,
                          "lng" : -50.9766
                       },
                       "southwest" : {
                          "lat" : 41.6765559,
                          "lng" : -141.00187
                       }
                    }
                 },
                 "place_id" : "ChIJ2WrMN9MDDUsRpY9Doiq3aJk",
                 "types" : [ "country", "political" ]
              }
           ],
           "status" : "OK"
        }
    ),
    15: ({
        "place_id": "ChIJ82ENKDJgHTERIEjiXbIAAQE"
        },
        {
           "results" : [
              {
                 "address_components" : [
                    {
                       "long_name" : "Bangkok",
                       "short_name" : "กทม",
                       "types" : [ "locality", "political" ]
                    },
                    {
                       "long_name" : "Thailand",
                       "short_name" : "TH",
                       "types" : [ "country", "political" ]
                    }
                 ],
                 "formatted_address" : "Bangkok, Thailand",
                 "geometry" : {
                    "bounds" : {
                       "northeast" : {
                          "lat" : 13.955111,
                          "lng" : 100.938408
                       },
                       "southwest" : {
                          "lat" : 13.4940881,
                          "lng" : 100.3278136
                       }
                    },
                    "location" : {
                       "lat" : 13.7563309,
                       "lng" : 100.5017651
                    },
                    "location_type" : "APPROXIMATE",
                    "viewport" : {
                       "northeast" : {
                          "lat" : 13.955111,
                          "lng" : 100.938408
                       },
                       "southwest" : {
                          "lat" : 13.4940881,
                          "lng" : 100.3278136
                       }
                    }
                 },
                 "place_id" : "ChIJ82ENKDJgHTERIEjiXbIAAQE",
                 "types" : [ "locality", "political" ]
              }
           ],
           "status" : "OK"
        }
    )

}
