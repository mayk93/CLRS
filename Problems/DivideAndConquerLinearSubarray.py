'''
Formal statement:
Input: An array for numbers, A.
Output: Information regarding the maximum subarray of A. (Start,End and Value)
Requirements: Linear running time.
'''

'''
In order to create a linear time algorithm that determines the maximum
subarray, we first need to construct an auxiliary array, S (suffixes or
subarray info) that tells us what is the maximum subarray ending at each index.
S[3] for example will tell us what is the maximum subarray ending at index 3.
'''

# This function returns maximum subarray information for A
def GetMaximumSubarrayInfo(A):
    if len(A) <= 0:
        print("Array A needs to have at least one element. None returned.")
        return None
    S = [{'left':0,'right':0,'sum':A[0]}]
    if len(A) == 1:
        return S
    # The subarray ending at 0 will start (left) at 0, end(right) at 0 and it's
    # sum is the element A[0]
    for (index,element) in enumerate(A[1:]):
        index += 1
        newInformation = {}
        # When we have a negative sum, we know not to add it, as it will lower
        # the lower the maximum value. Therefore, we reset left, right and sum
        # to the current element
        if (S[index-1]['sum'] < 0):
            newInformation = {'left':index,'right':index,'sum':element}
        # If we don't have a negative sum, we add it to the previous sum and
        # move to the right by one position (right+1)
        else:
            newInformation = {'left':S[index-1]['left'],'right':S[index-1]['right']+1,'sum':S[index-1]['sum']+element}
        S.append(newInformation)
    return S

# We iterate through the max-subarray-info array (S) in order to retrieve the
# information ('left','right','sum' touple) corresponding to the maximum
# subarray.
def GetMaximumSubarray(A):
    S = GetMaximumSubarrayInfo(A)
    if S == None:
        print("Array S needs to have at least one element. None returned.")
        return None
    maxSubarrayInfo = S[0]
    for element in S:
        if element['sum'] > maxSubarrayInfo['sum']:
            maxSubarrayInfo = element
    return maxSubarrayInfo

A = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]

print(GetMaximumSubarray(A))
