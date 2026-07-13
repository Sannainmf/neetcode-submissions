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

        # [1t, <- 2c, <- 3, -> 4p -> None]
        # 

        curr = prev
        prev = None
        k = 0

        while curr:
            k += 1
            if k == n:
                curr = curr.next
            else:
                t = curr.next
                curr.next = prev
                prev = curr
                curr = t

        return prev


        