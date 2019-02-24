#!/usr/bin/env python3

import random
import sys
import math

def get_random_direction():
    direction = ""
    probability = random.random()

    if probability < 0.25:
        direction = "west"
    elif probability < 0.5:
        direction = "north"
    elif probability < 0.75:
        direction = "south"
    else:
        direction = "east"

    return(direction)

def get_direction_displacement(dir_key):
    
    displacements = {
        'west': (-1, 0),
        'east': (1, 0),
        'north': (0, 1),
        'south': (0, -1)
        }

    # access the dictionary
    # UPDATE HERE: how do you use the key to access a dictionary?
    return(displacements[dir_key])

def take_walk(steps):
    current_location = [0, 0]
    for step_index in range(steps):
        direction = get_random_direction()
        displacement = get_direction_displacement(direction)

        # extract the numerical values from the tuple
        delta_x = displacement[0]
        delta_y = displacement[1]
        
        current_location[0] = current_location[0] + delta_x
        current_location[1] = current_location[1] + delta_y
        # UPDATE current_location HERE
        # consult example in 'Storing and Updating State' for method to update

    return(current_location)

def take_all_walks(steps, runs):
    endpoints = []
    for run_index in range(runs):
        end_location = take_walk(steps)
        endpoints.append(end_location)
    return endpoints

def average_final_distance(endpoints):
    total_distance = 0
    for coords in endpoints:
        dx = coords[0]
        dy = coords[1]

        # use the Pythagorean theorem to get distance like last session
        distance = math.sqrt(dx*dx + dy*dy)

        total_distance += distance

    return total_distance / len(endpoints)

# at end of __main__ code add these lines to see if it worked
# mind the indentation, should be 4 spaces in front
    average_displacement = average_final_distance(end_locations)
    print(average_displacement)


if __name__ == "__main__":
#    print(get_random_direction())
#    print(get_direction_displacement(get_random_direction()))
    steps = 15
    if len(sys.argv) > 1:
        steps = int(sys.argv[1])    
    
    runs = 1
    if len(sys.argv) > 2:
        runs = int(sys.argv[2])

    print("Donewith walking, printing end location: ")
    print(take_walk(steps))
    end_locations = (take_all_walks(steps,runs))
    print(average_final_distance(end_locations))
    


