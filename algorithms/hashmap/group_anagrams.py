# question link -> https://leetcode.com/problems/group-anagrams/description/?envType=study-plan-v2&envId=top-100-liked

"""
Solution - Time O(n * mlog(m)) | Space O(n * m)

- initialize a map that we are going to use to keep track of sorted string against all the strings which are anagrams of this sorted key.
- we are gonna start a loop through the given input array of strings.
- for every string we sort it, check if this sorted value is present in the map as a key - if yes add the original string into the array of values.
- otherwise add the sorted string as a new key in the map with a value of [originalStr].
- once the process is done - return the values of the map in an array.

"""

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagramsMap = {}
    for originalStr in strs:
        sortedStr = ''.join(sorted(originalStr))
        if sortedStr in anagramsMap:
            anagramsMap[sortedStr].append(originalStr)
        else:
            anagramsMap[sortedStr] = [originalStr]

    return list(anagramsMap.values())