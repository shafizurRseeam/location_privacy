import numpy as np
import random
import scipy.special
from haversine import haversine, inverse_haversine, Unit

from geo_utils import latitude_longitude_to_y_x, y_x_to_latitude_longitude, get_direction
from geo_utils import get_direction
from mechanism_staircase import planar_staircase_mechanism_point



def bounded_planar_staircase_mechanism_point(Location, noise_staircase_bounded):
    
    Latitude, Longitude = Location
    y, x = latitude_longitude_to_y_x(Latitude, Longitude)
    Noise_X, Noise_Y = random.choice(noise_staircase_bounded) 
    Perturbed_X = x + Noise_X
    Perturbed_Y = y + Noise_Y 
    Perturbed_Latitude, Perturbed_Longitude = y_x_to_latitude_longitude(Perturbed_Y, Perturbed_X)
    
    return Perturbed_Latitude, Perturbed_Longitude

def intermediate(dataset, noise_staircase_bounded):
    
    dataset = dataset.copy()  # Make a copy to avoid modifying the original DataFrame
    num_locations = len(dataset['Latitude'])

    # Initialize intermediate and final reported locations
    dataset['intermediate_lat'] = np.nan
    dataset['intermediate_lon'] = np.nan

    
    # Handle the first location separately
    true_location = (dataset['Latitude'][0], dataset['Longitude'][0])
    intermediate_location = bounded_planar_staircase_mechanism_point(true_location, noise_staircase_bounded)
    
    #distance_first = haversine(true_location, intermediate_location, unit=Unit.METERS)


    dataset.at[0, 'intermediate_lat'] = intermediate_location[0]
    dataset.at[0, 'intermediate_lon'] = intermediate_location[1]
    #dataset.at[0, 'distance_first'] = distance_first

    
    # Handle subsequent locations
    for i in range(1, num_locations):
        true_location = (dataset.at[i, 'Latitude'], dataset.at[i, 'Longitude'])
        last_true = (dataset.at[i-1, 'Latitude'], dataset.at[i-1, 'Longitude'])
        distance = haversine(true_location, last_true, unit=Unit.METERS)
        direction = get_direction(last_true, true_location)
        
        intermediate_location = inverse_haversine(
            (dataset.at[i-1, 'intermediate_lat'], dataset.at[i-1, 'intermediate_lon']),
            distance,
            direction,
            Unit.METERS
        )
        
        dataset.at[i, 'intermediate_lat'] = intermediate_location[0]
        dataset.at[i, 'intermediate_lon'] = intermediate_location[1]
        
        

    return dataset

# Update your existing intermediate function to include the generation of reported locations

def only_reported_locations(dataset, noise_staircase, delta):
    
    #dataset = intermediate(dataset, epsilon, x_interval, bl)  # Assume this generates intermediate locations y1, y2, ..., yn
    
    # Initialize the reported locations column
    dataset['Perturbed_Latitude'] = np.nan
    dataset['Perturbed_Longitude'] = np.nan
    
    # Handle the first location separately
#     dataset.at[0, 'Perturbed_Latitude'], dataset.at[0, 'Perturbed_Longitude'] = SSLLPM(
#         (dataset.at[0, 'intermediate_lat'], dataset.at[0, 'intermediate_lon'])
#     )
    
    
    dataset.at[0, 'Perturbed_Latitude'], dataset.at[0, 'Perturbed_Longitude'] = planar_staircase_mechanism_point(
        (dataset.at[0, 'intermediate_lat'], dataset.at[0, 'intermediate_lon']), noise_staircase)
    
    
    
    
    # Store the current focus point (start with the first point)
    current_focus = (dataset.at[0, 'Latitude'], dataset.at[0, 'Longitude'])
    current_reported = (dataset.at[0, 'Perturbed_Latitude'], dataset.at[0, 'Perturbed_Longitude'])
    
    # Iterate over the remaining locations
    for i in range(1, len(dataset)):
        
        true_location = (dataset.at[i, 'Latitude'], dataset.at[i, 'Longitude'])
        distance_from_focus = haversine(true_location, current_focus, unit=Unit.METERS)
        
        if distance_from_focus < delta:
            # If the distance is below the threshold, report the same location as the current reported location
            dataset.at[i, 'Perturbed_Latitude'] = current_reported[0]
            dataset.at[i, 'Perturbed_Longitude'] = current_reported[1]
        
        else:
            # If the distance is above the threshold, perturb the intermediate location to get the reported location
            dataset.at[i, 'Perturbed_Latitude'], dataset.at[i, 'Perturbed_Longitude'] = planar_staircase_mechanism_point(
                (dataset.at[i, 'intermediate_lat'], dataset.at[i, 'intermediate_lon']), noise_staircase
            )
            
            # Update the current focus and reported locations
            current_focus = true_location
            current_reported = (dataset.at[i, 'Perturbed_Latitude'], dataset.at[i, 'Perturbed_Longitude'])
    
    return dataset