from googlegeocoder import GoogleGeocoder
geocoder = GoogleGeocoder()
search = geocoder.get("Watts Towers")
print(search)
