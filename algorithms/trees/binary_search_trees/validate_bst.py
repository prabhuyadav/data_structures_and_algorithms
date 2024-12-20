# question link -> https://leetcode.com/problems/validate-binary-search-tree/description/?envType=study-plan-v2&envId=top-100-liked

"""
Solution - Time O(n) | Space O(h) - n is no.of nodes in the BST and h is height of the BST

- for each node, the left and right side trees should be a valid BST to consider the entire tree to be a valid BST.
- for each node, there is a lower bound and an upper bound that it should be in between - otherwise then the node is not a valid BST node - therefore the entire tree is not valid BST.
- for our root the lower, upper bounds are -Inf, +Inf
- when we are recursing to the left - update the upper bound to the root value (as left side node should be less than root).
- when we are recursing to the right - update the lower bound to the root value (as right side node should be greater than root).
- if the node is none then return true by default
"""


class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def validateBst(root: TreeNode) -> bool:
    lower, upper = float("-inf"), float("inf")
    return validateBstHelper(root, lower, upper)


def validateBstHelper(root, lower, upper):
    if root is None:
        return True

    if root.val >= upper or root.val <= lower:
        return False

    isLeftValid = validateBstHelper(root.left, lower, root.val)
    isRightValid = validateBstHelper(root.right, root.val, upper)

    return isLeftValid and isRightValid
