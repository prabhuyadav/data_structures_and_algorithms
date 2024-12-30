# question-link -> https://leetcode.com/problems/subsets/description/?envType=study-plan-v2&envId=top-100-liked

"""
Solution - Time O(n * 2^n) | Space O(n * 2^n)

- Given an array of numbers, we need to return an array of subsets.
- This is a simple recursion problem -> for every num in array - we consider each element in the current subset and append new possible combinations to the subset.
- The code will be self-explanatory so limiting the description for this solution approach.

"""


def subsets(nums: list[int]) -> list[list[int]]:
    powerSet = [[]]
    for num in nums:
        # we wanna only loop through the current existing elements of the powerSet, not the ones we are going to add during this loop.
        for i in range(len(powerSet)):
            subset = powerSet[i] + [num]
            powerSet.append(subset)
    return powerSet
