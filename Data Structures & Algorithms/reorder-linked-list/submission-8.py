# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        """
        test
        """

        curr = head
        arr = []

        while curr:
            arr.append(curr)
            curr = curr.next

        newArr = []
        l = 0
        r = len(arr) - 1

        while l <= r:
            newArr.append(arr[l])
            if l != r:
                newArr.append(arr[r])
            l += 1
            r -= 1
            
        dummy = ListNode()
        curr = dummy

        for element in newArr:
            curr.next = element
            curr = curr.next
        
        curr.next = None


        