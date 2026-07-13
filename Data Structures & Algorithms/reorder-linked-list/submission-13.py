# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        h = slow.next
        slow.next = None
        prev = None

        while h:
            t = h.next
            h.next = prev
            prev = h
            h = t

        end = prev
        start = head

        while end:
            t1 = start.next
            t2 = end.next
            start.next = end
            end.next = t1
            start = t1
            end = t2
        