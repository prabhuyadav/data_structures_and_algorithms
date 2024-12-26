# question link -> https://leetcode.com/problems/longest-consecutive-sequence/description/

"""
Solution - Time O(n) | Space O(n)

- we have to determine the longest consecutive sequence in the array and return its length.
- initialize a variable result to store our final answer
- initialize a hashmap - visited -> to store the values of the array as keys and False as the default value since we haven't visited them yet.
- now start a loop through the array - if the num we are considering is already visited then continue.
- if not - mark it as visited, then to determine the consecutive sequence that exists in the array in which the current num is part of, go left from this num until you encounter a num that's not in visited as a key (which means this num is not in array as well).
- similarly go right as well. keep track of the length that we have moved combined both left and right - so that gives us the consecutive sequence length that the current num is part of.
- update the result value to the maximum of (result, lengthOfCurrentConsecutiveSequence).

"""

def longestConsecutiveSequence(nums: list[int]) -> int:
    result = 0
    visited = {}
    for num in nums:
        visited[num] = False

    for num in nums:
        if visited[num]:
            continue

        visited[num] = True
        currentSequenceLength = 1

        left = num-1
        while left in visited:
            currentSequenceLength += 1
            visited[left] = True
            left -= 1

        right = num+1
        while right in visited:
            currentSequenceLength += 1
            visited[right] = True
            right += 1

        result = max(result, currentSequenceLength)

    return result