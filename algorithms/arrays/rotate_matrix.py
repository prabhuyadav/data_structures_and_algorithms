# question-link -> https://leetcode.com/problems/rotate-image/description/?envType=study-plan-v2&envId=top-100-liked

"""
Solution - O(n^2) Time | O(n^2) Space -> n is the number of rows/columns in the matrix.

- we wanna rotate a 2d array of n*n size in place 90deg clockwise.
- using trial and calculating initial and final positions of the elements we can deduce a formula using the index of an element.
- for an element at idx - [i, j] - after the matrix is rotated 90deg clockwise -> the position would be [j, n-1-i]
- the meat of this problem is to modify the array in place.
- we will keep another 2d array to mark whether an element in the array is visited or not.
- we will loop through the entire array, if the element is not visited - then we figure out the nextIdx for this element, store that nextIdx and it's value.
- place the current value in the nextIdx spot. now continue this pattern in a while loop until you find a nextIdx which we have already visited.
- by the time we finish for loop the array will be rotated in place entirely.

"""

def rotateMatrix(matrix: list[list[int]]):
    row, col = len(matrix)-1, len(matrix[0])-1
    visited = [[False for _ in range(col+1)] for _ in range(row+1)]

    for i in range(row+1):
        for j in range(col+1):
            if visited[i][j]:
                continue

            currentIdx, currentValue = [i, j], matrix[i][j]
            while not visited[currentIdx[0]][currentIdx[1]]:
                currentRow, currentCol = currentIdx[0], currentIdx[1]
                visited[currentRow][currentCol] = True

                nextIdx, nextValue = [currentCol, row-currentRow], matrix[currentCol][row-currentRow]
                matrix[nextIdx[0]][nextIdx[1]] = currentValue

                currentIdx, currentValue = nextIdx, nextValue
