#!/usr/bin/env python3

# Chris's code for calculating volume of a shape revolving around an axis.

def squarePoly(coList):
    prod = []
    for i in range(2 * len(coList) - 1):
        prod.append(0)
    for i in range(len(coList)):
        for j in range(len(coList)):
            prod[i + j] += coList[i] * coList[j]
    return prod

def intPoly(coList):
    intList = [0]
    for i in range(len(coList)):
        intList.append(coList[i] / (i + 1))
    return intList

def defIntRange(x1, x2, coList):
    total = 0
    for i in range(len(coList)):
        total += ((x2) ** i - (x1) ** i) * coList[i]
    return total

def printList(ls):
    for item in ls:
        print(item, end=' ')
    print()

def doEverything(coeff, highBound, lowBound, markVolume):
    volume = defIntRange(lowBound, highBound, intPoly(squarePoly(coeff))) * 3.14159
    print(round(volume, 2))
    
    height = lowBound
    iterVolume = 0.0
    nextMark = markVolume
    marks = []
    
    if volume > markVolume:
        
        while height < highBound:
            iterVolume = defIntRange(lowBound, height, intPoly(squarePoly(coeff))) * 3.14159
            
            if iterVolume > nextMark:
                if len(marks) < 8:
                    nextMark += markVolume
                    marks.append(round(height - lowBound, 2))
                else:
                    break
            height += .001
        printList(marks)
    else:
        print("insufficient volume")

case = 1
while True:
    try:
        length = input()
        polynomial = list(map(float, input().split(" ")))
        low, high, iterVolume = input().split(" ")
        low = float(low)
        high = float(high)
        iterVolume = float(iterVolume)

        print("Case", case, end=': ')
        case += 1
        doEverything(polynomial, high, low, iterVolume)
    except EOFError:
        break
