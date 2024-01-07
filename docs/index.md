# python-googlegeocoder

A simple Python wrapper for Google’s geocoder API

## Features

* Submit an address and have it geocoded
* Submit a lat/lng pair and have it reverse-geocoded
* Results include all data returned by Google, including formatted address, location, viewport, bounds, address type and address components
* Bias results to a bounding box you provide
* Bias results to a region you specify by country code
* Specify a language code
* Results automatically converted to WKT format

## Getting started

Installation

```bash
pip install python-googlegeocoder
```

Geocoding an address

```python
from googlegeocoder import GoogleGeocoder
geocoder = GoogleGeocoder("<YOUR GOOGLE MAPS API KEY>")
search = geocoder.get("Watts Towers")
search
[<GeocoderResult: Watts Towers Arts Center, 1727 E 107th St, Los Angeles, CA 90002-3621, USA>]
search[0].geometry.location
<Coordinates: (33.9395164, -118.2414404)>
print (search[0].geometry.location.lat, search[0].geometry.location.lng)
(33.9395164, -118.2414404)
```

Reverse geocoding coordinates

```python
reverse = geocoder.get((33.9395164, -118.2414404))
reverse
[<GeocoderResult: 1736 E 106th St, Los Angeles, CA 90002, USA>, <GeocoderResult: Watts, Los Angeles, CA, USA>, <GeocoderResult: Los Angeles, CA 90002, USA>, <GeocoderResult: South LA, Los Angeles, CA, USA>, <GeocoderResult: Los Angeles, CA, USA>, <GeocoderResult: Los Angeles, CA, USA>, <GeocoderResult: Los Angeles, California, USA>, <GeocoderResult: California, USA>, <GeocoderResult: United States>]
```

Viewport biasing

```python
before = geocoder.get("Winnetka")
before[0]
<GeocoderResult: Winnetka, IL, USA>
after = geocoder.get("Winnetka", bounding_box=((34.172684,-118.604794), (34.236144,-118.500938)))
after[0]
<GeocoderResult: Winnetka, Los Angeles, CA, USA>
```

Region biasing

```python
before = geocoder.get("Toledo")
before[0]
<GeocoderResult: Toledo, OH, USA>
after = geocoder.get("Toledo", region="ES")
after[0]
<GeocoderResult: Toledo, Spain>
```

Loop through a list of addresses and print out latitude, longitude and location type of the first result.

```python
from googlegeocoder import GoogleGeocoder
geocoder = GoogleGeocoder()
list_of_addresses = [
    '1727 E 107th St, Los Angeles, CA',
    '317 Broadway, Los Angeles, CA'
]
for address in list_of_addresses:
    try:
        search = geocoder.get(address)
    except ValueError:
        continue
    first_result = search[0]
    output =  [
        first_result.formatted_address,
        first_result.geometry.location.lat,
        first_result.geometry.location.lng,
        first_result.geometry.location_type
    ]
    print map(str, output)
```

## Other resources

* Repo: [https://github.com/datadesk/python-googlegeocoder](https://github.com/datadesk/python-googlegeocoder)
* Issues: [https://github.com/datadesk/python-googlegeocoder/issues](https://github.com/datadesk/python-googlegeocoder/issues)
* Packaging: [https://pypi.python.org/pypi/python-googlegeocoder](https://pypi.python.org/pypi/python-googlegeocoder)
* [Google's official documentation](http://code.google.com/apis/maps/documentation/geocoding/)
