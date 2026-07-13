# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        curr = head
        i = head
        prev = None

        while curr and curr.next:
            if curr == prev:
                return True
            prev = i
            i = i.next
            curr = curr.next.next

        return False

        