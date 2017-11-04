#!/usr/bin/env python3

case_amt = int(input())

for _ in range(case_amt):
    coins = []
    
    [N, Q] = map(int, input().split(' '))

    for i in range(11):
        coins.append(0)

    for _ in range(Q):
        line_info = list(map(int, input().split(' ')))
        if line_info[0] == 1:
            for i in range(line_info[1], line_info[2] + 1):
                coins[i % 10] += ((i % 10)) * line_info[3]
        elif line_info[0] == 2:
            for i in range(line_info[1], line_info[2] + 1):
                coins[i % 10] = 0
        elif line_info[0] == 3:
            total = 0
            for value in coins:
                total += value
            print(total)
