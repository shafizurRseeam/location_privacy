
import numpy as np
import random
import scipy.special



from mechanism_laplace import planar_laplace_mechanism_point
from haversine import haversine, Unit


def planar_laplace_mechanism_delta(dataset, noise_laplace, delta):

    dataset['Perturbed_Latitude'] = np.nan
    dataset['Perturbed_Longitude'] = np.nan
    dataset['Distance'] = np.nan
    dataset['prevdistance'] = np.nan

    true_location      = (dataset.at[0, 'Latitude'], dataset.at[0, 'Longitude'])            
    Perturbed_Location = planar_laplace_mechanism_point(true_location, noise_laplace)

           
    
    dataset.at[0, 'Perturbed_Latitude']  =  Perturbed_Location[0]
    dataset.at[0, 'Perturbed_Longitude'] =  Perturbed_Location[1]

            

    #dataset.at[0, 'prevdistance'] = 0

    distance = haversine(true_location, Perturbed_Location, unit = Unit.METERS)
    #dataset.at[0, 'Distance'] =  distance          

    current_focus = true_location
    current_reported = Perturbed_Location


    for i in range(1, len(dataset)):


        true_location = (dataset.at[i, 'Latitude'], dataset.at[i, 'Longitude'])
        
        distance_from_focus = haversine(true_location, current_focus, unit = Unit.METERS)
        dataset.at[i, 'prevdistance'] = distance_from_focus


        if distance_from_focus < delta:

            
            dataset.at[i, 'Perturbed_Latitude'] = current_reported[0]
            dataset.at[i, 'Perturbed_Longitude'] = current_reported[1]
                

            distance = haversine(true_location, (dataset.at[i, 'Perturbed_Latitude'], dataset.at[i, 'Perturbed_Longitude']), unit = Unit.METERS)


            #dataset.at[i, 'Distance'] =  distance

        else:

            Perturbed_Location = planar_laplace_mechanism_point(true_location, noise_laplace)

            
            dataset.at[i, 'Perturbed_Latitude']  =  Perturbed_Location[0]
            dataset.at[i, 'Perturbed_Longitude'] =  Perturbed_Location[1]

            distance = haversine(true_location, Perturbed_Location, unit = Unit.METERS)
            #dataset.at[i, 'Distance'] =  distance 

            
            current_reported = (dataset.at[i,'Perturbed_Latitude'], dataset.at[i,'Perturbed_Longitude'])
            current_focus    = (  dataset.at[i,'Latitude'], dataset.at[i,'Longitude'])


    return dataset
    