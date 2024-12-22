# question link -> https://leetcode.com/problems/binary-tree-level-order-traversal/description/?envType=study-plan-v2&envId=top-100-liked

"""
Solution - Time O(n) | Space O(n)

- we are going traverse the entire tree while keeping track of the level we are on during the traversal.
- initialize an empty array which we will fill up during the traversal with the required output
- we are going to pre-order traversal, which will guarantee us that the order of the values in the array for a level will be from left to right which is what we want.
- during the traversal, add the current node's value to the corresponding level(idx) in the array
- return the array at the end.

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root: TreeNode) -> list[list[int]]:
    values = []
    preOrderTraversal(root, 0, values)
    return values

def preOrderTraversal(tree: TreeNode, level: int, values: list[list[int]]):
    if tree is None:
        return

    if len(values) > level:
        values[level].append(tree.val)
    else:
        values.append([tree.val])

    preOrderTraversal(tree.left, level+1, values)
    preOrderTraversal(tree.right, level+1, values)