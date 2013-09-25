python-googlegeocoder
=====================

A simple Python wrapper for version three of Google's geocoder API

[![Build Status](https://travis-ci.org/datadesk/python-googlegeocoder.png?branch=master)](https://travis-ci.org/datadesk/python-googlegeocoder)

Features
--------

* Submit an address and have it geocoded
* Submit a lat/lng pair and have it reverse-geocoded
* Results include all data returned by Google, including formatted address, location, viewport, bounds, address type and address components
* Results automatically converted to WKT format
* Bias results to a bounding box you provide
* Bias results to a region you specify by country code
* Specify a language code
* No API key required

Getting started
---------------

Installation

```bash
$ pip install python-googlegeocoder
```

Geocoding an address

```python
>>> from googlegeocoder import GoogleGeocoder
>>> geocoder = GoogleGeocoder()
>>> search = geocoder.get("Watts Towers")
>>> search
[<GeocoderResult: Watts Towers Arts Center, 1727 E 107th St, Los Angeles, CA 90002-3621, USA>]
>>> search[0].geometry.location
<Coordinates: (33.9395164, -118.2414404)>
```

Reverse geocoding coordinates

```python
>>> reverse = geocoder.get((33.9395164, -118.2414404))
>>> reverse
[<GeocoderResult: 1736 E 106th St, Los Angeles, CA 90002, USA>, <GeocoderResult: Watts, Los Angeles, CA, USA>, <GeocoderResult: Los Angeles, CA 90002, USA>, <GeocoderResult: South LA, Los Angeles, CA, USA>, <GeocoderResult: Los Angeles, CA, USA>, <GeocoderResult: Los Angeles, CA, USA>, <GeocoderResult: Los Angeles, California, USA>, <GeocoderResult: California, USA>, <GeocoderResult: United States>]
```

Viewport biasing

```python
>>> before = geocoder.get("Winnetka")
>>> before[0]
<GeocoderResult: Winnetka, IL, USA>
>>> after = geocoder.get("Winnetka", bounding_box=((34.172684,-118.604794), (34.236144,-118.500938)))
>>> after[0]
<GeocoderResult: Winnetka, Los Angeles, CA, USA>
```

Region biasing

```python
>>> before = geocoder.get("Toledo")
>>> before[0]
<GeocoderResult: Toledo, OH, USA>
>>> after = geocoder.get("Toledo", region="ES")
>>> after[0]
<GeocoderResult: Toledo, Spain>
```

Iterate through a list of addresses and return latitude, longitude and location type

```python
>>> from googlegeocoder import GoogleGeocoder
>>> geocoder = GoogleGeocoder()
>>> list_of_addresses = ['1727 E 107th St, Los Angeles, CA', '317 Broadway, Los Angeles, CA']
>>> f = open("results.txt", "a")
>>> for address in list_of_addresses:
>>>     address = address.replace("\n","")
>>>     search = geocoder.get(address)
>>>     try:
>>>         address = str(search[0])
>>>         lat = str(search[0].geometry.location.lat)
>>>         lng = str(search[0].geometry.location.lng)
>>>         accuracy = str(search[0].geometry.location_type)
>>>         address_for_output = '%s\t%s\t%s\t%s\n' % (address, lat, lng, accuracy)
>>>     except ValueError:
>>>         address_for_output = 'ERROR\n'
>>>         print "We hit an error"
>>>     print address_for_output
>>>     f.write(address_for_output)
1727 East 107th Street, Los Angeles, CA 90002, USA	33.9386619	-118.2421333	RANGE_INTERPOLATED
317 Broadway, Los Angeles, CA 90013, USA	34.0505788	-118.2486735	ROOFTOP
```

Resources
---------

* [Google's official documentation](http://code.google.com/apis/maps/documentation/geocoding/)
