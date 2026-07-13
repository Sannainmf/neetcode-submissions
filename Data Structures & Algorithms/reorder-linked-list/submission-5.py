# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        curr = head
        arr = []

        while curr:
            arr.append(curr)
            curr = curr.next

        l = 0
        r = len(arr) - 1
        n = []

        while l <= r:
            n.append(arr[l])
            if l != r:
                n.append(arr[r])
            l += 1
            r -= 1

        dummy = ListNode()
        blud = dummy

        for element in n:
            blud.next = element
            blud = blud.next
        
        blud.next = None


        