
import numpy as np
import random
import scipy.special



from mechanism_laplace import planar_laplace_mechanism_point
from haversine import haversine, Unit


def planar_laplace_mechanism_delta(dataset, noise_laplace, delta):

    dataset['perturbed_latitude'] = np.nan
    dataset['perturbed_longitude'] = np.nan
    true_location      = (dataset.at[0, 'latitude'], dataset.at[0, 'longitude'])            
    Perturbed_Location = planar_laplace_mechanism_point(true_location, noise_laplace)
    dataset.at[0, 'perturbed_latitude']  =  Perturbed_Location[0]
    dataset.at[0, 'perturbed_longitude'] =  Perturbed_Location[1]
    distance = haversine(true_location, Perturbed_Location, unit = Unit.METERS)
             
    current_focus = true_location
    current_reported = Perturbed_Location

    for i in range(1, len(dataset)):

        true_location = (dataset.at[i, 'latitude'], dataset.at[i, 'longitude'])
        distance_from_focus = haversine(true_location, current_focus, unit = Unit.METERS)

        if distance_from_focus < delta:
      
            dataset.at[i, 'perturbed_latitude'] = current_reported[0]
            dataset.at[i, 'perturbed_longitude'] = current_reported[1]
                
            distance = haversine(true_location, (dataset.at[i, 'perturbed_latitude'], dataset.at[i, 'perturbed_longitude']), unit = Unit.METERS)

        else:

            Perturbed_Location = planar_laplace_mechanism_point(true_location, noise_laplace)
            
            dataset.at[i, 'perturbed_latitude']  =  Perturbed_Location[0]
            dataset.at[i, 'perturbed_longitude'] =  Perturbed_Location[1]

            distance = haversine(true_location, Perturbed_Location, unit = Unit.METERS)
           
            current_reported = (dataset.at[i,'perturbed_latitude'], dataset.at[i,'perturbed_longitude'])
            current_focus    = (  dataset.at[i,'latitude'], dataset.at[i,'longitude'])

    return dataset
    