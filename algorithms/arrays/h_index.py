# question-link -> https://leetcode.com/problems/h-index/description/

"""
Solution - Time O(n) | Space O(1)

- Given an array of integers, citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.
- The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

- when we consider a citation[i] to include it for sure, we have to know that this citation's value is greater than current h-index and the numbers that have contributed to this h-index are for sure greater than citation[i]
- this we can guarantee by sorting the array in descending order.
- initialize the h-index to zero.
- after sorting, we can start looping and then for every citation - we can check if it's value is greater than the current h-index - if so increase the h-index.
- As we are looping a sorted array in descending order, return the h-index when we encounter a citation that is less than or equal to h-index.

"""

def hIndex(citations: list[int]) -> int:
    value = 0
    citations.sort(reverse=True)

    for citation in citations:
        if citation <= value:
            return value
        value += 1

    return value
