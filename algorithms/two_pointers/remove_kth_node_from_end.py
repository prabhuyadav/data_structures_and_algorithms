# question link -> https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/?envType=study-plan-v2&envId=top-100-liked

"""
Solution(s) - Time O(n) | Space O(1)

Approach 1 (requires finding length of a linked list)

- find the length of the linked list with a loop - n.
- then kth node from the end is (n-k)th node from the start - so find the node to remove and undo the bindings of this node.

Approach 2 (two pointers).

- we can remove the kth node from the end, without having to find the length of the linked list using a two-pointer approach.
- initialize two pointers first and second to the head of the LL.
- advance the second pointer by k from the head. (i.e. second pointer is now (n-k+1) position away from the end of the LL - where n is the length of the LL)
- now if the second pointer is none after the above step - then the node that we need to remove is the head of the LL - do the process and return.
- if not, now start a loop where we advance both second and first pointers - so loop till second.next is none (i.e second travels n-k-1) - therefore first travels the same.
- so first will end up at (n-k-1)th position from the head - which is the node exactly before the kth node from the end - which is what we want to get to undo the bindings and remove the kth node from the LL.

"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeKthNodeFromEnd(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    # base case - where only one node is present in the LL, and our question constraints are that k is at-least 1.
    if head.next is None and k == 1:
        return None

    counter = 1
    first, second = head, head

    while counter < k + 1:
        second = second.next
        counter += 1

    if second is None:
        head.val = head.next.val
        head.next = head.next.next
        return head

    while second.next is not None:
        second = second.next
        first = first.next

    first.next = first.next.next
    return head
