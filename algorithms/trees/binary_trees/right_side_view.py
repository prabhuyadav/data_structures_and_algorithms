# question link -> https://leetcode.com/problems/binary-tree-right-side-view/?envType=study-plan-v2&envId=top-100-liked

"""
Solution - O(n) Time | O(n) Space

- we need to determine the right most node at every level of the tree - this is what the right side view of the tree consists.
- we can do this in a breadth-first search manner using a queue. initialize the queue with the root node in it.
- determine the number of the elements in the queue at the start of the loop - this gives us the range until which we need to loop. (i.e. we loop level by level)
- so in each step - we pop the left element in the queue and then add the child nodes of the current node to the queue.
- by the time we are done with above step - we will have added the children of current level nodes to the queue and the last popped node would be right most node in the current level (because we are gonna be adding the left child first and then the right child for every node that we process).
- we are gonna be encountering some None nodes during the above steps (just add conditional checks to skip those nodes).
- so add this last popped node to the result array which we will return at the end.

"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root: TreeNode) -> list[int]:
    queue = deque([root])
    result = []

    while queue:
        rightMostNodeAtCurrentLevel = None
        currentLevelLength = len(queue)

        for i in range(currentLevelLength):
            node = queue.popleft()
            if node:
                rightMostNodeAtCurrentLevel = node
                queue.append(node.left)
                queue.append(node.right)

        # After the for loop above - the value of this rightMostNodeAtCurrentLevel variable would actually be the right most node at the level that we processed.
        if rightMostNodeAtCurrentLevel:
            result.append(rightMostNodeAtCurrentLevel.val)

    return result
