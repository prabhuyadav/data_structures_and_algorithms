# question-link -> https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/?envType=study-plan-v2&envId=top-100-liked

"""
Solution - Time O(log(n)) | Space O(1)

- we can do an altered binary search for this question. we wanna fina a range of indices (i.e the first and last position of a target in our sorted array).
- we can do the searching twice - once to find the first idx, and the other to find the last idx of our target element in the array.
- during the normal binary search if the middle is not equal to our target - then we can go left or right based on middle value.
- if the middle is equal to the target, then we have to determine whether it's an extreme of the target or not.
- this is where having the logic of trying to find the leftmost/rightmost element lends itself useful to us.
- if you are trying to find the left most idx - then check whether middle idx is zero or if middle-1 is not target value and update accordingly.
- we'll do the same for the rightmost idx deduction as well.
- return [-1, -1] if the target is not found in the array

"""

def searchRange(nums: list[int], target: int) -> list[int]:
    finalRange = [-1, -1]

    alteredBinarySearch(finalRange, nums, target, 0, len(nums)-1, True)
    alteredBinarySearch(finalRange, nums, target, 0, len(nums)-1, False)

    return finalRange

def alteredBinarySearch(finalRange, array, target, left, right, goLeft):
    while left <= right:
        middle = (left + right) // 2
        if array[middle] > target:
            right = middle-1
        elif array[middle] < target:
            left = middle+1
        else:
            if goLeft:
                if middle == 0 or array[middle-1] != target:
                    finalRange[0] = middle
                    return
                else:
                    right = middle-1
            else:
                if middle == len(array)-1 or array[middle+1] != target:
                    finalRange[1] = middle
                    return
                else:
                    left = middle+1