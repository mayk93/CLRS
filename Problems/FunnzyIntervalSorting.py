import random

'''
This code needs bug fixing.
'''

class Interval:
    def __init__(self,left,right):
        self.left=left
        self.right=right
    def __str__(self):
        return "< Start: "+str(self.left)+" End: "+str(self.right)+" >"

def Intersects(interval,otherInterval):
    return interval.left <= otherInterval.right and otherInterval.left <= interval.right
def Before(interval,otherInterval):
    return interval.right < otherInterval.left
def After(interval,otherInterval):
    return interval.left > otherInterval.right

#Initially, start = 0 and end = len(A)
def Partition(A,start,end):
    randomIndex = random.randint(start,end-1) #We don't want to choose the length
    A[randomIndex],A[end-1]=A[end-1],A[randomIndex]
    intersection = A[end-1]

    for (index,element) in enumerate(A[:end-1]):
        index += start
        if(Intersects(intersection,element)):
            if(element.left > intersection.left):
                intersection.left = element.left
            if(element.right < intersection.right):
                intersection.right = element.right

    pivotLeft = start
    for (index,element) in enumerate(A[:end-1]):
        index += start
        if(Before(element,A[pivotLeft])):
            A[index],A[pivotLeft] = A[pivotLeft],A[index]
            pivotLeft += 1
    A[end-1],A[pivotLeft] = A[pivotLeft],A[end-1]

    pivotRight = pivotLeft+1
    index = end-1
    while(pivotRight <= index):
        index += start
        if(Intersects(element,intersection)):
            A[pivotRight],A[index] = A[index],A[pivotRight]
            pivotRight += 1
        else:
            index -= 1

    return Interval(pivotLeft,pivotRight)

def IntervalSort(A,start,end):
    if start < end-1:
        pivot = Partition(A,start,end)
        IntervalSort(A,start,pivot.left)
        IntervalSort(A,pivot.right,end)

def Display(A):
    return [str(element) for element in A]

#A = [Interval(abs(random.randint(0,5)),abs(random.randint(6,10))) for i in range(0,3)]
A = [Interval(2,8),Interval(3,9),Interval(2,6)]
print("Before: "+str(Display(A)))
IntervalSort(A,0,len(A))
print("After: "+str(Display(A)))
