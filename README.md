python-googlegeocoder
=====================

A simple Python wrapper for version three of Google's geocoder API.

[![Build Status](https://travis-ci.org/datadesk/python-googlegeocoder.png?branch=master)](https://travis-ci.org/datadesk/python-googlegeocoder)
[![PyPI version](https://badge.fury.io/py/python-googlegeocoder.png)](http://badge.fury.io/py/python-googlegeocoder)
[![Coverage Status](https://coveralls.io/repos/datadesk/python-googlegeocoder/badge.png?branch=master)](https://coveralls.io/r/datadesk/python-googlegeocoder?branch=master)

* Docs: [python-googlegeocoder.rtfd.org](http://python-googlegeocoder.rtfd.org)
* Issues: [github.com/datadesk/python-googlegeocoder/issues](https://github.com/datadesk/python-googlegeocoder/issues)
* Packaging: [pypi.python.org/pypi/python-googlegeocoder](https://pypi.python.org/pypi/python-googlegeocoder)
* Testing: [travis-ci.org/datadesk/python-googlegeocoder](https://travis-ci.org/datadesk/python-googlegeocoder)
* Coverage: [coveralls.io/r/datadesk/python-googlegeocoder](https://coveralls.io/r/datadesk/python-googlegeocoder)

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