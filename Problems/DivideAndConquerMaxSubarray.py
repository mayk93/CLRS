import sys

def maxCrossSubarray(A):
    middle = len(A)/2
    leftSum = -sys.maxsize
    leftLow = middle
    currentSum = 0
    for (i,element) in enumerate(reversed(A[:middle])):
        currentSum += element
        if currentSum > leftSum:
            leftSum = currentSum
            leftLow = middle-i-1
    rightSum = -sys.maxsize
    rightHigh = middle
    currentSum = 0
    for (i,element) in enumerate(A[middle:]):
        currentSum += element
        if currentSum > rightSum:
            rightSum = currentSum
            rightHigh = middle+i
    return (leftLow,rightHigh,leftSum+rightSum)

def maxSubarray(A):
    if len(A) == 1:
        return (0,0,A[0])
    middle = len(A)/2
    (leftLow,leftHigh,leftSum) = maxSubarray(A[:middle])
    (rightLow,rightHigh,rightSum) = maxSubarray(A[middle:])
    (crossLow,crossHigh,crossSum) = maxCrossSubarray(A)
    if leftSum >= rightSum and leftSum >= crossSum:
        return (crossLow,crossHigh,crossSum)
    elif rightSum >= leftSum and rightSum >= crossSum:
        return (rightLow,rightHigh,rightSum)
    else:
        return (crossLow,crossHigh,crossSum)

A = [1,-5,10,-3,2,3,1,0,6,10,-12,5,2,1,2]
print(maxCrossSubarray(A))
B = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
print(maxSubarray(B))
C = [-2,-3,-3,-4,-5,2]
print(maxSubarray(C))
