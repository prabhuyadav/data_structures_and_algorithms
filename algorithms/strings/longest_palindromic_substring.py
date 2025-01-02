# question-link -> https://leetcode.com/problems/longest-palindromic-substring/description/?envType=study-plan-v2&envId=top-100-liked

"""
Solution - Time O(n^2) | Space O(n)

- keep an array to store and update the first and last idx of the palindromes we find.
- for every character in the string - we can determine whether if its part of a valid palindrome (other than the single char itself).
- for every character - we go outwards left and right comparing characters and calculating the palindrome length.
- the character could be part of a palindrome two ways, i.e. it is part of a palindrome which has odd length and the current chart is exactly middle element.
- the other possibility is that it's part of a palindrome of even length - so the current char would have corresponding mirror char in the palindrome.
- we consider both cases and determine the odd and even possible palindrome lengths and consider the max len out of it.

"""

def longestPalindromicLength(s: str) -> str:
    currentLongest = [0, 1]
    for i in range(len(s)):
        oddPalindrome = getPalindromeLengthFrom(s, i-1, i+1)
        evenPalindrome = getPalindromeLengthFrom(s, i-1, i)
        longestPalindrome = max(oddPalindrome, evenPalindrome, key=lambda x: x[1]-x[0])
        currentLongest = max(currentLongest, longestPalindrome, key=lambda x: x[1]-x[0])

    return s[currentLongest[0]: currentLongest[1]]


def getPalindromeLengthFrom(string, leftIdx, rightIdx):
    while leftIdx >= 0 and rightIdx < len(string):
        if string[leftIdx] != string[rightIdx]:
            break
        leftIdx -= 1
        rightIdx += 1
    return [leftIdx+1, rightIdx]