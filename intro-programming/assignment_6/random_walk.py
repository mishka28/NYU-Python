#!/usr/bin/env python3

import random

def get_random_direction():
    direction = ""
    probability = random.random()

    if probability < 0.25:
        direction = "west"
    elif probability < 0.5:
        direction = "north"
    elif probability < 0.75:
        direction = "sounth"
    else:
        direction = "east"

    return(direction)

def get_direction_displacement(get_random_direction):
#    direction = "'" + direction +"'"
    get_random_direction = "'" + str(get_random_direction) + "'"
    displacements = {
        'west': (-1, 0),
        'east': (1, 0),
        'north': (0, 1),
        'south': (0, -1)
        }

    # access the dictionary
    # UPDATE HERE: how do you use the key to access a dictionary?
    # replace None with the answer
#    return(displacements[direction])
    return(displacements[get_random_direction])


if __name__ == "__main__":
    print(get_random_direction())
    print(get_direction_displacement(get_random_direction))
