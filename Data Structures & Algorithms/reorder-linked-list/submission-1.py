# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        """
        Id say first we traverse the linked list to get the length of  it.

        Once we have the length, we go thru it again and for every other node, we try to
        find the node at n - 1, where 1 decrements by 1
        """

        curr = head
        arr = []
        newArr = []
        

        while curr:
            arr.append(curr)
            curr = curr.next

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

        for e in newArr:
            curr.next = e
            curr = curr.next

        curr.next = None

        

            





            
            
            
        