#!/usr/bin/env python3

# 2016 South Central USA, problem 7997

def get_max(grade_str, amt):
    if amt == 1:
        if grade_str == '' or int(grade_str) > 100:
            raise Exception('invalid grade')
        return int(grade_str)

    possible_results = []

    if grade_str[:3] == '100':
        try:
            possible_results.append(int(grade_str[:3]) +
                                    get_max(grade_str[3:], amt - 1))
        except:
            pass

    try:
        possible_results.append(int(grade_str[:2]) +
                                get_max(grade_str[2:], amt - 1))
    except:
        pass

    try:
        possible_results.append(int(grade_str[:1]) +
                                get_max(grade_str[1:], amt - 1))
    except:
        pass

    return max(possible_results)

def get_max_avg(grade_str, amt):
    return round(get_max(grade_str, amt) / amt)

students = int(input())

for i in range(students):
    amt, grade_str = input().split(' ')
    print(get_max_avg(grade_str, int(amt)))
