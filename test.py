import geopy

geolocator = geopy.Nominatim()

with open('playgrounds.txt', 'r') as file:
    for line in file:
        values = line.split("\t")
        if len(values) == 6 and values[0] != 'Town':
            (town, address, status, facilities, age_group, disable_access) = values
            play = '%s %s playground' % (town,address)
            location = geolocator.geocode("%s" % play)
            try:
                getattr(location, 'address')
            except AttributeError:
                print (play)
            else:
                print('%s, %s,%s' % (play,location.latitude, location.longitude))


