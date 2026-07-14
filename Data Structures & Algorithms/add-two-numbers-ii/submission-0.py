# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        res = ""

        curr = l1
        prev = None

        while curr:
            t = curr.next
            curr.next = prev
            prev = curr
            curr = t

        eq1 = prev

        curr = l2
        prev = None

        while curr:
            t = curr.next
            curr.next = prev
            prev = curr
            curr = t

        eq2 = prev

        remainder = 0

        while eq1 or eq2:

            total = 0

            if not eq1:
                total = eq2.val + remainder
            elif not eq2:
                total = eq1.val + remainder
            else:
                total = eq1.val + eq2.val + remainder

            result = total % 10
            remainder = total // 10

            res = str(result) + res

            if eq1:
                eq1 = eq1.next
                
            if eq2:
                eq2 = eq2.next

        if remainder != 0:
            res = str(remainder) + res

        dummy = ListNode(0)
        curr = dummy

        for num in res:
            curr.next = ListNode(int(num))
            curr = curr.next

        return dummy.next

        

        

        
        