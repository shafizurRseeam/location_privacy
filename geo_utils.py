import numpy as np
import math

EARTH_RADIUS = 6371000

def latitude_longitude_to_y_x(latitude, longitude):
    x = EARTH_RADIUS * np.radians(longitude)
    y = EARTH_RADIUS * np.radians(latitude)
    return y, x

def y_x_to_latitude_longitude(y, x):
    longitude = np.degrees(x / EARTH_RADIUS)
    latitude = np.degrees(y / EARTH_RADIUS)
    return latitude, longitude

def get_direction(loc1, loc2):
    dLon = (loc2[1] - loc1[1])

    y = math.sin(math.radians(dLon)) * math.cos(math.radians(loc2[0]))
    x = math.cos(math.radians(loc1[0])) * math.sin(math.radians(loc2[0])) - math.sin(math.radians(loc1[0])) * math.cos(math.radians(loc2[0])) * math.cos(math.radians(dLon))
    brng = math.atan2(y, x)
    return brng

#test to see changes
#further test to see if it works
