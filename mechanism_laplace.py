import numpy as np
import random
import scipy.special

from geo_utils import latitude_longitude_to_y_x, y_x_to_latitude_longitude




def planar_laplace_mechanism_point(location, noise_laplace):
    latitude, longitude = location
    y, x = latitude_longitude_to_y_x(latitude, longitude)
    noise_x, noise_y = random.choice(noise_laplace)
    Perturbed_X = x + noise_x
    Perturbed_Y = y + noise_y
    Perturbed_Latitude, Perturbed_Longitude = y_x_to_latitude_longitude(Perturbed_Y, Perturbed_X)
    
    return Perturbed_Latitude, Perturbed_Longitude



def planar_laplace_mechanism(dataset, noise_laplace):
    
    dataset['perturbed_latitude'] = np.nan
    dataset['perturbed_longitude'] = np.nan
    #dataset['Distance'] = np.nan

    
    for i in range(len(dataset)):
        
        latitude = dataset.at[i, 'latitude']
        longitude = dataset.at[i, 'longitude']
        true_location = (latitude, longitude)
        perturbed_location= planar_laplace_mechanism_point(true_location, noise_laplace)

        #distance = haversine(true_location, perturbed_location, unit = Unit.METERS)
        dataset.loc[i, 'perturbed_latitude'] = perturbed_location[0]
        dataset.loc[i, 'perturbed_longitude'] = perturbed_location[1]
    
    return dataset


