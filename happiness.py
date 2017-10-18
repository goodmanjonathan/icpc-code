#!/usr/bin/env python3

# Southeast USA 2012 6222

def happify(num):
    sum_of_squares = 0
    for c in str(num):
        sum_of_squares += int(c) ** 2
    return sum_of_squares

def happiness_distance(num):
    used_list = []
    iterations = 0

    while(True):
        if num in used_list:
            return -1 # num is unhappy
        used_list.append(num)

        if num == 1:
            return iterations
        
        num = happify(num)
        iterations += 1

def count_unhappies(lower, upper):
    unhappies = 0
    for i in range(lower, upper + 1):
        if happiness_distance(i) == -1:
            unhappies += 1

    return unhappies

while True:
    lower, upper = map(int, input().split(' '))
    if lower == 0 and upper == 0:
        break
    
    print(count_unhappies(lower, upper))
