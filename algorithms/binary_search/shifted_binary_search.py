# question link -> https://leetcode.com/problems/search-in-rotated-sorted-array/?envType=study-plan-v2&envId=top-100-liked

"""
Solution - Time O(log(n)) | Space O(1)
- start two pointers left and right with values as 0 and len(nums)-1 respectively.
- we are going to do binary search but the internal logic needs to be modified as the array is sorted, but also it's shifted.
- start a while loop till left <= right
- find the middle idx
- if the middle value is greater than our target - then we need to check if the left value is > target and left value is <= middle - in this case our target is on the right side, otherwise it's on the left side.
- if the middle value is less than our target - then we need to check if the right value is < target and right value is >= middle - in this case our target is on the left side, otherwise it's on the right side.
- if the middle idx value is our target return the idx.
- if the target isn't found then return -1.

- the hint is to that when the array is shifted by a pivot idx, and you are at an idx(middle) - only one side of the array is sorted (left-middle) or (middle-right) including the middle.
- so we check for a condition that will eliminate one half of the array.

"""

def shifted_binary_search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if target < nums[middle]:
            if target < nums[left] <= nums[middle]:
                left = middle + 1
            else:
                right = middle - 1
        elif target > nums[middle]:
            if target > nums[right] >= nums[middle]:
                right = middle - 1
            else:
                left = middle + 1
        else:
            return middle

    return -1


