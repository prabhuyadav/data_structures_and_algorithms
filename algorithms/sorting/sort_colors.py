# question-link -> https://leetcode.com/problems/sort-colors/description/?envType=study-plan-v2&envId=top-100-liked

"""
Solution - O(n) Time | O(1) Space

- we need to sort the array in the order of 0, 1, 2 in place. we're given an array of only those three nums.
- we can do this in two steps - bring all the 0s to the start of the array and then 2s to the end of the array.
- the 1s will automatically end up being in the middle.
- traverse the array while keeping track of another idx which signifies the position that needs to be swapped.
- during the traversal, the idx will keep on increasing if we encounter the number 0 then that needs to be swapped.
- when we encounter a 0, then we swap the idx and the placerIdx and then increment the placerIdx. we don't increment the placerIdx if nums[idx] is not zero.
- once we are done with the loop, all the 0s come to the front of the array.
- we'll do the same thing from the end for 2s.

"""

def sortColors(nums: list[int]) -> None:
    firstPlacerIdx = 0
    for idx in range(len(nums)):
        if nums[idx] == 0:
            nums[idx], nums[firstPlacerIdx] = nums[firstPlacerIdx], nums[idx]
            firstPlacerIdx += 1

    thirdPlacerIdx = len(nums)-1
    for idx in reversed(range(len(nums))):
        if nums[idx] == 2:
            nums[idx], nums[thirdPlacerIdx] = nums[thirdPlacerIdx], nums[idx]
            thirdPlacerIdx -= 1