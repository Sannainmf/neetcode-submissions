# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        curr = head
        arr = []
        
        while curr:
            arr.append(curr)
            curr = curr.next

        dummy = ListNode()
        t = dummy

        for i in range(len(arr)):
            if i == len(arr) - n:
                continue

            t.next = arr[i]
            t = t.next

        t.next = None

        return dummy.next
                
            
        