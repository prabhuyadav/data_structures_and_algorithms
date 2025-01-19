class Heap:
    def __init__(self, comparisonFunc, array):
        self.comparisonFunc = comparisonFunc
        self.heap = self.buildHeap(array)
        self.length = len(self.heap)

    # Time O(n) | Space O(1)
    def buildHeap(self, array):
        largestParentIdx = getParentIdx(len(array)-1)
        for idx in reversed(range(largestParentIdx+1)):
            self.siftDown(idx, array)
        return array

    # Time O(log(n)) | Space O(1)
    def siftDown(self, idx, heap):
        childIdx = self.getChildIdxToSwap(idx, heap)
        while childIdx >= 0 and self.comparisonFunc(heap[childIdx], heap[idx]):
            swap(idx, childIdx, heap)
            idx = childIdx
            childIdx = self.getChildIdxToSwap(idx, heap)

    # Time O(log(n)) | Space O(1)
    def siftUp(self, idx, heap):
        parentIdx = getParentIdx(idx)
        while parentIdx >= 0 and self.comparisonFunc(heap[idx], heap[parentIdx]):
            swap(idx, parentIdx, heap)
            idx = parentIdx
            parentIdx = getParentIdx(idx)

    # Time O(1) | Space O(1)
    def peek(self):
        return self.heap[0]

    # Time O(log(n)) | Space O(1)
    def remove(self):
        swap(self.length-1, 0, self.heap)
        valueToRemove = self.heap.pop()
        self.length -= 1
        self.siftDown(0, self.heap)
        return valueToRemove

    # Time O(log(n)) | Space O(1)
    def insert(self, value):
        self.heap.append(value)
        self.length += 1
        self.siftUp(self.length-1, self.heap)

    # Time O(1) | Space O(1)
    def getChildIdxToSwap(self, idx, heap):
        childIndices = getChildIndices(idx, heap)
        if len(childIndices) == 0:
            return -1
        if len(childIndices) == 1:
            return childIndices[0]

        childIdxOne, childIdxTwo = childIndices
        return childIdxOne if self.comparisonFunc(heap[childIdxOne], heap[childIdxTwo]) else childIdxTwo


# Utility functions that are used in the class methods.
def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

def getParentIdx(idx):
    return (idx - 1) // 2

def getChildIndices(idx, heap):
    childIdxOne, childIdxTwo = 2 * idx + 1, 2 * idx + 2
    indices = []
    if childIdxOne < len(heap):
        indices.append(childIdxOne)
    if childIdxTwo < len(heap):
        indices.append(childIdxTwo)
    return indices

# comparison functions which will determine the behavior of the heap, i.e., whether MAX_HEAP or MIN_HEAP
def MAX_HEAP_FUNC(a, b):
    return a > b

def MIN_HEAP_FUNC(a, b):
    return a < b

