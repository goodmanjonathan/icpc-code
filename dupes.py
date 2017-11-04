#!/usr/bin/env python3

case_amt = int(input())

for _ in range(case_amt):
    sentence = input().split(' ')

    duped = False
    for word in sentence:
        if sentence.count(word) > 1:
            duped = True
            break
    if duped == False:
        print('yes')
    else:
        print('no')
    
    # for wordi in range(len(sentence)):
    #     if sentence[wordi] in sentence[:wordi] 
