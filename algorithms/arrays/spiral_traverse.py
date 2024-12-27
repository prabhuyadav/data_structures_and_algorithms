# question link -> https://leetcode.com/problems/spiral-matrix/?envType=study-plan-v2&envId=top-100-liked

"""
Solution - Time O(n) | Space O(n)

- we need to traverse a 2D matrix spirally and return a 1D array with the result.
- this question is more about the way you implement and how clean your code is in handling the edge cases of the spiral traversing.
- so there won't be much explanation of the algorithm as it is self-explanatory.

"""

def spiralTraverse(matrix: list[list[int]]) -> list[int]:
    n, m = len(matrix), len(matrix[0])
    startRowIdx, endRowIdx = 0, n-1
    startColIdx, endColIdx = 0, m-1

    spiralArray = []
    while startRowIdx < endRowIdx and startColIdx < endColIdx:
        for idx in range(startColIdx, endColIdx+1):
            spiralArray.append(matrix[startRowIdx][idx])
        startRowIdx += 1

        for idx in range(startRowIdx, endRowIdx+1):
            spiralArray.append(matrix[idx][endColIdx])
        endColIdx -= 1

        for idx in reversed(range(startColIdx, endColIdx+1)):
            spiralArray.append((matrix[endRowIdx][idx]))
        endRowIdx -= 1

        for idx in reversed(range(startRowIdx, endRowIdx+1)):
            spiralArray.append(matrix[idx][startColIdx])
        startColIdx += 1

    if startColIdx == endColIdx or startRowIdx == endRowIdx:
        for i in range(startRowIdx, endRowIdx+1):
            for j in range(startColIdx, endColIdx+1):
                spiralArray.append(matrix[i][j])

    return spiralArray