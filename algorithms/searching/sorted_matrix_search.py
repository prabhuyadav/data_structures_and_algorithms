# question link -> https://leetcode.com/problems/search-a-2d-matrix-ii/description/?envType=study-plan-v2&envId=top-100-liked

"""
Solution - O(n+m) Time | O(1) Space - where our matrix is of dimensions m*n.

- the matrix rows and cols are sorted, and we have to find a target.
- we can solve this efficiently by picking the right start index to start our search with in the matrix.
- best way is to start from the last idx in the first row i.e. (0, col)
- if this element is greater than our target element then we can decrement the colIdx, if its lesser then we can increment the rowIdx or else return true.
- perform this logic in a while loop until the rowIdx, colIdx are out of bounds.

"""

def searchInSortedMatrix(matrix: list[list[int]], target: int) -> bool:
    row, col = len(matrix), len(matrix[0])
    rowIdx, colIdx = 0, col-1

    while rowIdx < row and colIdx > -1:
        if matrix[rowIdx][colIdx] < target:
            rowIdx += 1
        elif matrix[rowIdx][colIdx] > target:
            colIdx -= 1
        else:
            return True
    return False
