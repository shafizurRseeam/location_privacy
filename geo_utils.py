import numpy as np

EARTH_RADIUS = 6371000

def latitude_longitude_to_y_x(latitude, longitude):
    x = EARTH_RADIUS * np.radians(longitude)
    y = EARTH_RADIUS * np.radians(latitude)
    return y, x

def y_x_to_latitude_longitude(y, x):
    longitude = np.degrees(x / EARTH_RADIUS)
    latitude = np.degrees(y / EARTH_RADIUS)
    return latitude, longitude
