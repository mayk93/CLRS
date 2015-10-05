import copy

class Heap(object):
    def __init__(self,array=[]):
        self.array = array
        self.length = len(array)
        self.heapSize = len(array)
    def __str__(self):
        tree = self.Tree()
        return ('---\n'+'Heap:\n'+str(self.array)+'\nArray Length: '+str(self.length)+'\nHeap Size: '+str(self.heapSize)+'\nTree:\n'+tree+'\n---\n')
    def Tree(self):
        tree = ""
        for (index,element) in enumerate(self.array):
            tree += "Children of " + str(element) + " on position " + str(index) + " are: " + (str(self.array[Left(index)]) if Left(index) < self.heapSize else "NIL") + " and " + (str(self.array[Right(index)]) if Right(index) < self.heapSize else "NIL") + "\n"
        return tree
    def getLength(self):
        return len(self.array)
    def setLength(self,value):
        self.array = self.array[:value]
        if len(self.array) < self.heapSize:
            self.heapSize = len(self.array)
    def delLength(self):
        self.array = []
    def getHeapSize(self):
        return self.__heapSize
    def setHeapSize(self,value):
        self.heapSize = value if value < len(self.array) else len(self.array)
    def delHeapSize(self):
        self.__heapSize = 0
    __length = property(getLength,setLength,delLength,"Length proprety.")
    __heapSize = property(getHeapSize,setHeapSize,delHeapSize,"Heap size proprety.")

def Left(i):
    return 2*i+1
def Right(i):
    return 2*i+2
def Parent(i):
    if i == 0 or 1:
        return 0
    return i/2-1
# The Swap function is deprecated.
'''
def Swap(A,i,j):
    a = A[i]
    b = A[j]
    A.pop(i)
    A.insert(i,b)
    A.pop(j)
    A.insert(j,a)
'''
# Max Heapify Implementations
'''
We get the indices of the current element's (A[i]) children, using Left and
Right. We compare the value of the current element to that of his children.
If one of the children is learger than the element, that child takes it's place.
We recursively call the function to ensure the Max Heap Propriety is preserved
in case we make a swap.
'''
def MaxHeapifyRecursiveInplace(H,i):
    if H.length <= 0:
        print("This heap is empty. Returned none.")
        return
    if H.length == 1:
        return
    left = Left(i)
    right = Right(i)
    largest = i
    if left < H.heapSize and H.array[left] > H.array[i]:
        largest = left
    if right < H.heapSize and H.array[right] > H.array[largest]:
        largest = right
    if largest != i:
        #Swap(H.array,i,largest)
        H.array[i],H.array[largest] = H.array[largest],H.array[i]
        MaxHeapifyRecursiveInplace(H,largest)

def MaxHeapifyRecursiveNewHeap(H,i):
    if H.length <= 1:
        print("This heap is empty.")
        return copy.deepcopy(H)
    if H.length == 1:
        return copy.deepcopy(H)
    left = Left(i)
    right = Right(i)
    largest = i
    newHeap = copy.deepcopy(H)
    if left < newHeap.heapSize and newHeap.array[left] > newHeap.array[i]:
        largest = left
    if right < newHeap.heapSize and newHeap.array[right] > newHeap.array[largest]:
        largest = right
    if largest != i:
        newHeap.array[i],newHeap.array[largest] = newHeap.array[largest],newHeap.array[i]
        MaxHeapifyRecursiveInplace(newHeap,largest)
    return newHeap

def MaxHeapifyIterativeInplace(H,i):
    if H.length <= 0:
        print("This heap is empty.")
        return
    if H.length == 1:
        return
    while True:
        left = Left(i)
        right = Right(i)
        largest = i
        if left < H.heapSize and H.array[left] > H.array[i]:
            largest = left
        if right < H.heapSize and H.array[right] > H.array[largest]:
            largest = right
        if i == largest:
            return
        else:
            H.array[i],H.array[largest] = H.array[largest],H.array[i]
        i = largest

def MaxHeapifyIterativeNewHeap(H,i):
    if H.length <= 0:
        print("This heap is empty.")
        return copy.deepcopy(H)
    if H.length == 1:
        return copy.deepcopy(H)
    newHeap = copy.deepcopy(H)
    while True:
        left = Left(i)
        right = Right(i)
        largest = i
        if left < newHeap.heapSize and newHeap.array[left] > newHeap.array[i]:
            largest = left
        if right < newHeap.heapSize and newHeap.array[right] > newHeap.array[largest]:
            largest = right
        if i == largest:
            return newHeap
        else:
            newHeap.array[i],newHeap.array[largest] = newHeap.array[largest],newHeap.array[i]
        i = largest

# Min Heapify Implementations
def MinHeapifyRecursiveInplace(H,i):
    if H.length <= 0:
        print('This heap is empty.')
        return
    if H.length == 1:
        return
    left = Left(i)
    right = Right(i)
    smallest = i
    if left < H.heapSize and H.array[left] < H.array[i]:
        smallest = left
    if right < H.heapSize and H.array[right] < H.array[smallest]:
        smallest = right
    if smallest != i:
        H.array[i],H.array[smallest] = H.array[smallest],H.array[i]
        MinHeapifyRecursiveInplace(H,smallest)

def MinHeapifyRecursiveNewHeap(H,i):
    if H.length <= 0:
        print('This heap is empty.')
        return copy.deepcopy(H)
    if H.length == 1:
        return copy.deepcopy(H)
    left = Left(i)
    right = Right(i)
    smallest = i
    newHeap = copy.deepcopy(H)
    if left < newHeap.heapSize and newHeap.array[left] < newHeap.array[i]:
        smallest = left
    if right < newHeap.heapSize and newHeap.array[right] < newHeap.array[smallest]:
        smallest = right
    if smallest != i:
        newHeap.array[i],newHeap.array[smallest] = newHeap.array[smallest],newHeap.array[i]
        MinHeapifyRecursiveInplace(newHeap,smallest)
    return newHeap

def MinHeapifyIterativeInplace(H,i):
    if H.length <= 0:
        print("This heap is empty.")
        return
    if H.length == 1:
        return
    while True:
        left = Left(i)
        right = Right(i)
        smallest = i
        if left < H.heapSize and H.array[left] < H.array[i]:
            smallest = left
        if right < H.heapSize and H.array[right] < H.array[smallest]:
            smallest = right
        if i == smallest:
            return
        else:
            H.array[i],H.array[smallest] = H.array[smallest],H.array[i]
        i = smallest

def MinHeapifyIterativeNewHeap(H,i):
    if H.length <= 0:
        print("This heap is empty.")
        return copy.deepcopy(H)
    if H.length == 1:
        return copy.deepcopy(H)
    newHeap = copy.deepcopy(H)
    while True:
        left = Left(i)
        right = Right(i)
        smallest = i
        if left < newHeap.heapSize and newHeap.array[left] < newHeap.array[i]:
            smallest = left
        if right < newHeap.heapSize and newHeap.array[right] < newHeap.array[smallest]:
            smallest = right
        if i == smallest:
            return
        else:
            newHeap.array[i],newHeap.array[smallest] = newHeap.array[smallest],newHeap.array[i]
        i = smallest
    return newHeap

def BuildHeap(H,function=MaxHeapifyRecursiveInplace):
     for (index,element) in enumerate(reversed(H.array[(H.length)/2:])):
        index = H.length/2-index
        try:
            print(index)
            function(H,index)
        except Exception as e:
            print("Exception:")
            print(str(e))

def GetHeap(H,function=MaxHeapifyRecursiveInplace):
     newHeap = copy.deepcopy(H)
     for (index,element) in enumerate(reversed(newHeap.array[(newHeap.length)/2:])):
        index = newHeap.length/2-index
        try:
            function(newHeap,index)
        except Exception as e:
            print("Exception:")
            print(str(e))
     return newHeap

def HeapSortInplace(A):
    H = GetHeap(Heap(A))
    for index,element in enumerate(H.array[::-1]):
        index = H.length - index - 1
        H.array[0],H.array[index] = H.array[index],H.array[0]
        H.heapSize -= 1
        MaxHeapifyRecursiveInplace(H,0)
    for element in H.array:
        A.pop(0)
        A.append(element)

def HeapSortNewArray(A):
    H = GetHeap(Heap(A))
    for index,element in enumerate(H.array[::-1]):
        index = H.length - index - 1
        H.array[0],H.array[index] = H.array[index],H.array[0]
        H.heapSize -= 1
        MaxHeapifyRecursiveInplace(H,0)
    newArray = []
    for element in H.array:
        newArray.append(element)
    return newArray
