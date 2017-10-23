#!/usr/bin/env python3

# Southeast USA 2012 6223

# orientation should be 'x' or 'y'
def place_wall(wall_axis, region):
    region.sort(key=lambda wall: wall[wall_axis])
    bisect_location = len(region) / 2

def check_bisect(wall_axis, wall_loc, region):
    before_count = 0
    after_count = 0

    for location in region:
        if location.wall_axis < wall_loc:
            before_count += 1
        else:
            after_count += 1

    return abs(after_count - before_count) <= 1

# returns number of walls needed for a region
def place_walls(region):
    if len(region) <= 3:
        return len(region) - 1

    

def input_region():
    wall_amount = int(input())
    regions = [[]]
    for i in range(wall_amount):
        x, y = tuple(map(int, input().split(' ')))
    return region
    
start_region = input_region()

