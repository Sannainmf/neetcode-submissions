# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        curr = head
        another = head
        prev = None

        while curr and curr.next:
            if curr == prev:
                return True
            prev = another
            another = another.next
            curr = curr.next
            curr = curr.next

        return False

        