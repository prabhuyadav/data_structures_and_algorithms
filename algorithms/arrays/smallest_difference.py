# question-link -> https://www.algoexpert.io/questions/smallest-difference

# Time O(nlog(n)) + O(mlog(m)) | Space O(1)
def smallestDifference(arrayOne: list[int], arrayTwo: list[int]):
    arrayOne.sort()
    arrayTwo.sort()
    idxOne, idxTwo = 0, 0
    smallest, current = float("inf"), float("inf")
    smallestPair = []

    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]
        if firstNum < secondNum:
            current = secondNum - firstNum
            idxOne += 1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            idxTwo += 1
        else:
            return [firstNum, secondNum]

        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]

    return smallestPair