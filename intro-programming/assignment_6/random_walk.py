#!/usr/bin/env python3

import random
import sys

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

if __name__ == "__main__":
#    print(get_random_direction())
#    print(get_direction_displacement(get_random_direction()))
    steps = 15
    if len(sys.argv) > 1:
        steps = int(sys.argv[1])    
    print("Donewith walking, printing end location: ")
    print(take_walk(steps))
    


