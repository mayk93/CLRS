#!/usr/local/bin/python3

from random import randrange
from statistics import median

def IndexedMedian(candidates):
    return sorted(candidates,key=lambda x:x[1])[1]

def RandomPivot(A,start,end,verbose=False):
    if start >= end:
        return
    if verbose:
        print("The array A, as was given: "+str(A))
    if len(A) <= 2:
        if verbose:
            print("Array A: "+str(A)+" was not modified.")
        return
    medianCandidates = []
    numberOfTries = 0
    while len(medianCandidates) < 3 and numberOfTries < 150:
        index = randrange(start,end)
        medianCandidates.append( (index,A[index]) )
        medianCandidates = list(set(medianCandidates))
        numberOfTries += 1
        if verbose:
            print("At this iteration ( "+str(numberOfTries)+" ), the median candidates are: "+str(medianCandidates))
    if len(medianCandidates) < 3:
        pivotIndex,pivot = medianCandidates[0]
    elif len(medianCandidates) == 3:
        if verbose:
            print("The final median candidates are: "+str(medianCandidates))
        pivotIndex,pivot = IndexedMedian(medianCandidates)
        if verbose:
            print("The pivot, the median of "+str(medianCandidates)+" is: "+str(pivot)+" at index: "+str(pivotIndex))
        A[end-1],A[pivotIndex] = A[pivotIndex],A[end-1]
        if verbose:
            print("The array now, after moving the pivot to the last place: "+str(A))


def Partition(A,start,end,verbose=False):
    if start >= end:
        return
    if verbose:
        print("Array before random pivot: "+str(A))
    RandomPivot(A,start,end,verbose)
    if verbose:
        print("Array before partition: "+str(A))
    pivot = A[end-1]
    pivotIndex = start-1
    for (index,element) in enumerate(A[start:end-1]):
        index += start
        if verbose:
            print("Current index: "+str(index))
        if element < pivot:
            pivotIndex += 1
            A[index],A[pivotIndex] = A[pivotIndex],A[index]
    pivotIndex += 1
    A[end-1],A[pivotIndex] = A[pivotIndex],A[end-1]
    if verbose:
        print("Array after partition: "+str(A))
    return pivotIndex

def QuickSelect(A,start,end,i,verbose=False):
    if verbose:
        print("Given array: "+str(A))
    if start >= end:
        if verbose:
            print("Start: "+str(start))
            print("End: "+str(end))
            print("A: "+str(A))
            print("A[start:end]: "+str(A[start:end]))
        if start < len(A):
            return A[start]
        else:
            return A[len(A)-1]
    pivotIndex = Partition(A,start,end,verbose)
    numberOfSmallerElements = pivotIndex - start
    if verbose:
        print("There are "+str(numberOfSmallerElements)+" smaller than "+str(A[pivotIndex]))
        print("Please check: "+str(A))
        print("Pivot at index: "+str(pivotIndex))
    if i == numberOfSmallerElements:
        if verbose:
            print("There are "+str(i)+"smaller elements than "+str(A[pivotIndex])+" in A, therefore A["+str(pivotIndex)+"] is good.")
            print("Check: "+str(A))
        return A[pivotIndex]
    elif i < numberOfSmallerElements:
        if verbose:
            print("Low side: ")
            print("Low Start: "+str(start))
            print("Low End: "+str(pivotIndex-1))
            print("A: "+str(A))
            print("A[ls:le]: "+str(A[start:pivotIndex]))
        return QuickSelect(A,start,pivotIndex-1,i,verbose)
    else:
        if verbose:
            print("High side: ")
            print("High Start: "+str(pivotIndex+1))
            print("High End: "+str(end))
            print("A: "+str(A))
            print("A[ls:le]: "+str(A[pivotIndex+1:end]))
        return QuickSelect(A,pivotIndex+1,end,i,verbose)


'''
def RandomPivot(A,start,end):
    B = A[start:end]
    if len(B) > 2:
        medianCandidates = []
        while len(medianCandidates) != 3:
            medianCandidates.append(B[randrange(0,len(B))])
            medianCandidates = list(set(medianCandidates))
        pivot = median(medianCandidates)
    else:
        pivot = B[randrange(0,len(B))]
    index = A.index(pivot)
    A[index],A[end-1] = A[end-1],A[index]

def Partition(A,start,end):
    RandomPivot(A,start,end)
    pivot = A[end-1]
    finalPivotIndex = start-1
    for (index,element) in enumerate(A[start:end]):
        index += start
        if element < pivot:
            finalPivotIndex += 1
            A[finalPivotIndex],A[index] = A[index],A[finalPivotIndex]
    A[finalPivotIndex],A[end-1] = A[end-1],A[finalPivotIndex]
    return finalPivotIndex

def QuickSelect(A,start,end,i): # i as in ith smallest element
    print("-----")
    print("The entire array: "+str(A))
    if start >= end or len(A[start:end]) == 1:
        if start < len(A):
            return A[start]
        else:
            return A[len(A)-1]
    pivotIndex = Partition(A,start,end)
    print("We chose as pivot: "+str(A[pivotIndex])+" at index: "+str(pivotIndex))
    print("The array after partition: "+str(A))
    print("Looking for the "+str(i)+" smallest element in array: "+str(A[start:end]))
    numberOfSmallerElements = pivotIndex - start + 1 # Smaller than the pivot
    print("There are "+str(numberOfSmallerElements)+" elements smaller than the pivot.")
    if i == numberOfSmallerElements:
        print("Therefore, the pivot, "+str(A[pivotIndex])+" is the "+str(i)+" smallest element.")
        return A[pivotIndex]
    elif i < numberOfSmallerElements:
        print("Therefore, we search for the "+str(i)+" smallest element on the array: "+str(A[start:pivotIndex]))
        return QuickSelect(A,start,pivotIndex,i)
    else:
        print("Therefore, we search for the "+str(i-numberOfSmallerElements)+" smallest element on the array: "+str(A[pivotIndex+1:end]))
        return QuickSelect(A,pivotIndex+1,end,i-numberOfSmallerElements)
