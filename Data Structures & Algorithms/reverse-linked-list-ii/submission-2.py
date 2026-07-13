# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head
        s = dummy
        e = dummy

        counter = 0

        while counter < left - 1:
            s = s.next
            counter += 1

        counter = 0

        while counter < right + 1:
            e = e.next
            counter += 1

        l = s.next

        r = dummy
        counter = 0
        while counter < right:
            r = r.next
            counter += 1

        r.next = None
        prev = None
        curr = l

        while curr:
            t = curr.next
            curr.next = prev
            prev = curr
            curr = t

        s.next = r
        l.next = e

        return dummy.next

        