# question link -> https://leetcode.com/problems/find-all-anagrams-in-a-string/?envType=study-plan-v2&envId=top-100-liked

"""
Solution - Time - O(n * m) | Space - O(m) - where n is len(s), m is len(p)

- if the len of p > s then return empty array.
- keep a dict of char count for p - dictA
- keep another dict that we use to track the char count while looping s. - dictB
- initialize startIdx = 0, endIdx = len(p)-1, store the char count for this substr in dictB.
- start a loop now - while endIdx < len(s).
- check if the two dicts are equal in keys/values - i.e. this substring is an anagram to p. update our result.
- next step is slide the window by 1.
- update dictB accordingly.

"""


def findAnagrams(s: str, p: str) -> list[int]:
    if len(s) < len(p):
        return []

    startIdx, endIdx = 0, len(p)-1
    dictA, dictB = {}, {}
    result = []

    for char in p:
        dictA[char] = (dictA.get(char) or 0) + 1

    for char in s[:endIdx+1]:
        dictB[char] = (dictB.get(char) or 0) + 1

    while endIdx < len(s):
        # update dictB char count to account for the slided window
        if startIdx != 0:
            prevChar = s[startIdx-1]
            dictB[prevChar] -= 1
            if dictB[prevChar] == 0:
                del dictB[prevChar]

            newChar = s[endIdx]
            dictB[newChar] = (dictB.get(newChar) or 0) + 1

        # compare dicts and update our result if they are equal (i.e., we found a substr in s that is anagram to p).
        if dictA == dictB:
            result.append(startIdx)

        # this is where we are sliding the window.
        startIdx += 1
        endIdx += 1

    return result

    pass