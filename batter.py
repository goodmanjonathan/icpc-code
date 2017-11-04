#!/usr/bin/env python3

batter_amt = int(input())

for _ in range(batter_amt):
    at_bats = int(input())
    result_list = list(map(int, input().split(' ')))
    #print(result_list)
    
    result_total = 0
    atbats = 0
    for result in result_list:
        if result >= 0:
            result_total += result
            atbats += 1

    print('{:.6f}'.format(result_total / atbats))
