# question-link -> https://www.algoexpert.io/questions/three-number-sum

# Time O(n^2) | Space O(n)

def threeNumberSum(array, targetSum):
    array.sort()
    triplets = []

    for i in range(len(array)-2):
        left, right = i+1, len(array)-1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left += 1
            else:
                right -= 1
    return  triplets


