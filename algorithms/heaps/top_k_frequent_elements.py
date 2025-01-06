# question-link -> https://leetcode.com/problems/top-k-frequent-elements/description/?envType=study-plan-v2&envId=top-100-liked

"""
Solution - Time O(n + (k * log(n))) | Space O(n)

- loop through the array and figure out the frequencies of each num in the input. keep track of this in a map.
- add the map (key,value) pairs in a list.
- max heapify the above list.
- pick the top k elements in this heap and return.

"""

import heapq

def topKFrequent(nums: list[int], k: int) -> list[int]:
    numMap = {}
    for num in nums:
        numMap[num] = (numMap.get(num) or 0) + 1

    numFrequencies = [[-1*v, n] for _, (n, v) in enumerate(numMap.items())]
    heapq.heapify(numFrequencies)

    topKFrequentElements = [n for _, n in heapq.nsmallest(k, numFrequencies)]

    return topKFrequentElements