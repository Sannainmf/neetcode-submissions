# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        curr = head
        prev = None

        while curr:
            t = curr.next
            curr.next = prev
            prev = curr
            curr = t

        # [None 4, p2, c1 ]

        i = 1
        curr = prev
        prev = None

        while curr:
            if i == n:
                curr = curr.next
            else:
                t = curr.next
                curr.next = prev
                prev = curr
                curr = t
            i += 1       

        return prev    
            
        