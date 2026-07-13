# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # <- 0 -> 1 -> 2 -> 3 -> None

        curr = head
        prev = None

        while curr:
            t = curr.next
            curr.next = prev
            prev = curr
            curr = t
        
        return prev






        