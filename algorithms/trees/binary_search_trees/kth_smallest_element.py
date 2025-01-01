# question-link -> https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/?envType=study-plan-v2&envId=top-100-liked

"""
Solution - Time O(h+k) | Space O(h)

- we are traverse the left sub-tree first and the right next for every node.
- during the traversal we keep track of the number of nodes visited and the latest visited node value - which can be used to return later.
- we need to consider a node visited only if all the left children of that node have been traversed, since we wanna find the kth smallest element.

"""

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self, numOfNodesVisited = 0, latestVisitedNodeValue = None):
        self.numOfNodesVisited = numOfNodesVisited
        self.latestVisitedNodeValue = latestVisitedNodeValue

def kthSmallestElement(root: TreeNode, k: int) -> int:
    treeInfo = TreeInfo()
    inOrderTraversal(root, treeInfo, k)
    return treeInfo.latestVisitedNodeValue

def inOrderTraversal(tree: TreeNode, treeInfo: TreeInfo, k: int):
    if tree is None or treeInfo.latestVisitedNodeValue == k:
        return

    inOrderTraversal(tree.left, treeInfo, k)
    if treeInfo.numOfNodesVisited < k:
        treeInfo.numOfNodesVisited += 1
        treeInfo.latestVisitedNodeValue = tree.val
        inOrderTraversal(tree.right, treeInfo, k)