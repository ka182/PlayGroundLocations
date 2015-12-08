import geopy

geolocator = geopy.Nominatim()

with open('playgrounds_loc.txt', 'r') as file:
    for line in file:
        values = line.split(",")
        if len(values) == 1:
            (park) = values[0].rstrip('\n')
            play = '%s' % (park)
            location = geolocator.geocode("%s" % play)
            try:
                getattr(location, 'address')
            except AttributeError:
                None
            else:
                print('%s, %s,%s' % (play,location.latitude, location.longitude))
        elif len(values) == 3:
            (playground, lat, lon) = (values[0], values[1], values[2].rstrip('\n'))
            print('%s,%s,%s' % (playground, lat, lon))


