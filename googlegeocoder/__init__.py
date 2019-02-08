"""
A simple Python wrapper on version 3 of Google's geocoder API.
"""
import os
import six
from six.moves import urllib
try:
    import json
except ImportError:
    import simplejson as json


class GoogleGeocoder(object):
    """
    A simple wrapper on version 3 of Google's geocoder API
    """
    BASE_URI = 'https://maps.googleapis.com/maps/api/geocode/json'

    def __init__(self, key=None):
        key = key or os.getenv("GOOGLE_MAPS_API_KEY")
        if not key:
            raise Exception("An API key is required by Google.")
        self.key = key

    def _fetch_json(self, params):
        """
        Configure a HTTP request, fire it off and return the response.
        """
        params = urllib.parse.urlencode(params, doseq=True)
        request = urllib.request.Request(self.BASE_URI + "?" + params)
        response = urllib.request.urlopen(request)
        return json.loads(response.read().decode("utf-8"))

    def get(self, submission, sensor='false', bounding_box=None, region=None,
            language=None):
        params = {
            'sensor': sensor,
            'key': self.key
        }
        if isinstance(submission, six.string_types):
            params['address'] = submission
        elif len(submission) == 2:
            params['latlng'] = ",".join(map(str, submission))
        else:
            raise ValueError("Your submission could not be parsed.")
        if bounding_box:
            if len(bounding_box) != 2:
                raise ValueError("You have submitted a bad bounding box.")
            # ... then tack it on the end.
            params['bounds'] = "%s,%s|%s,%s" % (
                bounding_box[0][0], bounding_box[0][1],
                bounding_box[1][0], bounding_box[1][1]
            )
        if region:
            params['region'] = region
        if language:
            params['language'] = language
        data = self._fetch_json(params)
        if data['status'] != "OK":
            raise ValueError(data["status"])
        return [GeocoderResult(i) for i in data.get("results")]


class UnicodeMixin(object):
    """
    Mixin class to handle defining the proper __str__/__unicode__
    methods in Python 2 or 3.
    """
    # Python 3
    if six.PY3:
        def __str__(self):
            return self.__unicode__()
    # Python 2
    else:
        def __str__(self):
            return self.__unicode__().encode('utf8')


class BaseAPIObject(UnicodeMixin):
    """
    A generic object to be returned by the API
    """
    def __init__(self, d):
        self.__dict__ = d

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self.__str__())


class GeocoderResult(BaseAPIObject):
    """
    A results objects returned by the API.

    Contains the following attributes:

        formatted_address: A string containing the human-readable address of
            this location. Often this address is equivalent to the
            "postal address," which sometimes differs from country to country

        types: A list that indicates the type of the returned result. This
            array contains a set of one or more tags identifying the type of
            feature returned in the result. For example, a geocode of "Chicago"
            returns "locality" which indicates that "Chicago" is a city, and
            also returns "political" which indicates it is a political entity.

        address_components: A list of the different parts of the address
            as AddressComponent class objects

        geometry: A collection of geometric data about the result, packaged
            as a Geoometry class object
    """
    def __init__(self, d):
        self.__dict__ = d
        self.address_components = [
            AddressComponent(i) for i in self.address_components
        ]
        self.geometry = Geometry(self.geometry)

    def __unicode__(self):
        return u'%s' % self.formatted_address


class AddressComponent(BaseAPIObject):
    """
    A piece of an address returned by the API

    Contains the following attributes:

        long_name: The full text description or name of the address component
            as returned by the Geocoder.

        short_name: is an abbreviated textual name for the address component,
            if available. For example, an address component for the state of
             Alaska may have a long_name of "Alaska" and a short_name of "AK"
            using the 2-letter postal abbreviation

        type: A list indicating the type(s) of the address component.
    """
    def __unicode__(self):
        return u'%s' % self.long_name


class Geometry(BaseAPIObject):
    """
    A collection of geometric data about a geocoder result.

    Contains the following attributes:

        location: The geocoded latitude and longitude as a Coordinate object.

        location_type: Additional meta data about the location, could be:
            "ROOFTOP", "RANGE_INTERPOLATED", "GEOMETRIC_CENTER", "APPROXIMATE"

        viewport: The recommended viewport for the returned result, returned as
            a Bounds class object.

        bounds: The bounding box that fully contains the result
            but may be bigger than the recommended viewport.

        partial_match: Indicates that the geocoder did not return an exact
            match for the original request, though it did match part of the
            requested address
    """
    def __init__(self, d):
        self.__dict__ = d
        if hasattr(self, "bounds"):
            self.bounds = Bounds(self.bounds)
        else:
            self.bounds = None
        self.viewport = Bounds(self.viewport)
        self.location = Coordinates(self.location)
        self.partial_match = hasattr(self, "partial_match")

    def __repr__(self):
        return '<%s>' % (self.__class__.__name__)

    def __unicode__(self):
        return u'Geometry'


class Bounds(BaseAPIObject):
    """
    A bounding box that contains the `southwest` and `northeast` corners
    as lnt/lng pairs.
    """
    def __init__(self, d):
        self.__dict__ = d
        self.southwest = Coordinates(self.southwest)
        self.northeast = Coordinates(self.northeast)

    def __unicode__(self):
        return u'(%s, %s)' % (self.southwest, self.northeast)


class Coordinates(BaseAPIObject):
    """
    A lat/lng pair.
    """
    def __unicode__(self):
        return u'(%s, %s)' % (self.lat, self.lng)

    @property
    def wkt(self):
        return 'POINT(%s %s)' % (self.lng, self.lat)
