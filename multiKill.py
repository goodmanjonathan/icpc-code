######
#  2013 South Central Regionals
#  Multikill
######

import math

def distance(xy1, xy2, radius): ## distance between two points
    dx = xy1[0] - xy2[0]
    dy = xy1[0] - xy2[1]
    dist = math.sqrt(dx*dx + dy*dy)
    if dist <= radius:          ## if distance within radius increment
        return 1  
    else:
        return 0

coords = [[1,0],[0,0],[1,0],[1,1],[5,5]]  # I just hardcoded this for now.  Same answer even if you put [5,5] coordinate first in list.
radius = 3
total = 0                       ## total of zombies within radius of a specific coordinate point
finalTotal = 0                  ## greatest total of zombies that are within radius range of one another


for pair1 in range(len(coords)):             ## check each xy pair with every other xy pair 
    for pair2 in range(len(coords)):
        if coords[pair1] == coords [pair2]:  ## if the current xy pair is being compared to itself then increment total 
            total += 1
        else:
            total += distance(coords[pair1], coords[pair2], radius)  ## if current xy pair is within radius or other xy pair, increment zombie count
    if total > finalTotal:     ## if number of zombies within radius is greater than previous total number, then replace greatest total
        finalTotal = total     
        total = 0
    else:
        total = 0
print (finalTotal)
    
    
    
    
    
