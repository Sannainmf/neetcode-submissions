# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #[1, 2s, 3s, 4] f
        #[1, 2, 3s, 4, 5f]

        #[1, 2s, 3, 4f]
        #[1, 2, 3s, 4, 5] f

        # s.next is second

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        prev = None

        while second:
            t = second.next
            second.next = prev
            prev = second
            second = t
        
        # prev is head now (of reversed linked list)

        first = head
        second = prev

        # [1, c2, tt3, c4, 5]

        # [1, 5, 2, 4, 3]

        while second:
            t1 = first.next
            t2 = second.next
            first.next = second
            second.next = t1
            first = t1
            second = t2
        

            







        



        