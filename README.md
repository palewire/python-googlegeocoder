=====================
python-googlegeocoder
=====================

A simple Python wrapper for version three of Google's geocoder API

[![Build Status](https://travis-ci.org/datadesk/python-documentcloud.png?branch=master)](https://travis-ci.org/datadesk/python-documentcloud)

Features
--------

* Submit an address and have it geocoded
* Submit a lat/lng pair and have it reverse-geocoded
* Results include all data returned by Google, including formatted address, location, viewport, bounds, address type and address components
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


