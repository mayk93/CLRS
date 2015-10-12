#!/usr/local/bin/python3

from random import randrange
from statistics import median

def Normalize(start,end,firstThird,secondThird):
    auxEnd = end
    if start == firstThird:
        firstThird += 1
    if firstThird + 1 == secondThird:
        secondThird += 1
    if secondThird + 1 == end:
        auxEnd = end+1
    return firstThird,secondThird,auxEnd

def RandomPivot(A,start,end):
    if (end-start) < 3:
        return
    '''
    A = [ ... start ... end ... ]
    We split the [start ... end] array like thid:
    firstThird = [start ... firstThird]
    secondThird = [firstThird+1 ... secondThird]
    thirdThird = [secondThird+1 ... end]
    '''
    firstThird = int(end/3)
    secondThird = int((2*end)/3)
    firstThird,secondThird,auxEnd = Normalize(start,end,firstThird,secondThird)
    print("["+str(start)+ " - " +str(firstThird)+"]" + "["+str(firstThird+1)+ " - " +str(secondThird)+"]" + "["+str(secondThird+1)+ " - " +str(auxEnd)+"]")
    medianCandidates = [A[randrange(start,firstThird)],A[randrange(firstThird+1,secondThird)],A[randrange(secondThird+1,auxEnd)]]
    medianValue = median(medianCandidates)
    medianIndex = A.index(medianValue)
    A[end],A[medianIndex] = A[medianIndex],A[end]

def Partition(A,start,end):
    RandomPivot(A,start,end)
    pivot = A[end]
    pivotIndex = start-1
    for currentIndex in range(start,end):
        if A[currentIndex] < pivot:
            pivotIndex += 1
            A[currentIndex],A[pivotIndex]=A[pivotIndex],A[currentIndex]
    pivotIndex += 1
    A[end],A[pivotIndex] = A[pivotIndex],A[end]
    return pivotIndex

def QuickSelectAux(A,start,end,ismallest):
    if end < start:
        print("Error!")
        return
    if start == end:
        return A[start]
    pivotIndex = Partition(A,start,end)
    numberOfElementsSmallerThanPivot = pivotIndex - start
    if ismallest == numberOfElementsSmallerThanPivot:
        return A[pivotIndex]
    elif ismallest < numberOfElementsSmallerThanPivot:
        return QuickSelectAux(A,start,pivotIndex-1,ismallest)
    elif ismallest > numberOfElementsSmallerThanPivot:
        # We use numberOfElementsSmallerThanPivot-ismallest because there are allready numberOfElementsSmallerThanPivot smaller than the pivot.
        # We need to use the difference.
        return QuickSelectAux(A,pivotIndex+1,end,numberOfElementsSmallerThanPivot-ismallest)


def QuickSelect(A,ismallest):
    return QuickSelectAux(A,0,len(A)-1,ismallest)

A = [9,0,2,5,1,7,4,3,6,8]
print(A)
for x in range(0,15):
    print("The "+str(x)+" smallest element is: "+str(A[QuickSelect(A,x)])+" at index: "+str(QuickSelect(A,x)))
print(A)
