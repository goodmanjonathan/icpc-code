#!/usr/bin/env python3

test_amt = int(input())

def diff(case1, case2):
    diff_count = 0
    for i in range(len(case1)):
        if case1[i] != case2[i]:
            return True
    return False

def find_unlike_substring(case1, case2):
    start = None
    end = None
    for i in range(len(case1)):
        if case1[i] != case2[i]:
            start = i
            break
    for i in range(len(case1) - 1, -1, -1):
        if case1[i] != case2[i]:
            end = i + 1
            break
            
    return (start, end)

def flip_count(case):
    return

def handle_case(str1, str2):
    unlike_substr = find_unlike_substring(str1, str2)
    if unlike_substr[1] - unlike_substr[0] == len(str1):
        print(0)
        return

    flipcount = 1
    for i in range(min(unlike_substr[0], len(str1) - unlike_substr[1])):
        if i == 0:
            continue
        try:
            test_substr1 = str1[unlike_substr[0] - i : unlike_substr[1]]
            test_substr2 = str2[unlike_substr[0] - i : unlike_substr[1]]
            if test_substr1 == test_substr2[::-1]:
                flipcount += 1
        except:
            pass
        try:
            test_substr1 = str1[unlike_substr[0]: unlike_substr[1] + i]
            test_substr2 = str2[unlike_substr[0]: unlike_substr[1] + i]
            if test_substr1 == test_substr2[::-1]:
                flipcount += 1
        except:
            pass
        try:
            test_substr1 = str1[unlike_substr[0] - i : unlike_substr[1] + i]
            test_substr2 = str2[unlike_substr[0] - i : unlike_substr[1] + i]
            if test_substr1 == test_substr2[::-1]:
                flipcount += 1
        except:
            pass
    print(flipcount)


for _ in range(test_amt):
    str1 = input()
    str2 = input()
    handle_case(str1, str2)

