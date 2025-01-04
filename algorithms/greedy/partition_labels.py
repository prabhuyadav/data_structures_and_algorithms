# question-link -> https://leetcode.com/problems/partition-labels/?envType=study-plan-v2&envId=top-100-liked

"""
Solution - O(n) Time | O(n) Space

- loop through the string and build a character frequency map
- We want to partition the string into as many parts as possible so that each letter appears in at most one part
- Start another loop now on the string - and keep reducing the char freq count in the map as you progress
- whenever a freq count for the chars in the map that we encounter becomes zero, we can be sure that this can be a partition that satisfies the condition.
- keep track of the encountered chars during the traversal.

"""

def partitionLabels(s: str) -> list[int]:
    charFrequencyMap = {}
    for char in s:
        charFrequencyMap[char] = (charFrequencyMap.get(char) or 0) + 1

    result = []
    encounteredChars = set([])
    partitionIdx = -1

    for i in range(len(s)):
        char = s[i]
        encounteredChars.add(char)
        charFrequencyMap[char] -= 1

        if not charFrequencyMap[char]:
            encounteredChars.remove(char)

        if not len(encounteredChars):
            result.append(i-partitionIdx)
            partitionIdx = i

    if not result:
        result.append(len(s))

    return  result