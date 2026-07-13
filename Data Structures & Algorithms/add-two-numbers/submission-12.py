# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:



        carry = 0
        dummy = ListNode()
        curr = dummy

        while l1 or l2:
            if not l1:
                s = l2.val + carry
            elif not l2:
                s = l1.val + carry
            else:
                s = l1.val + l2.val + carry

            r = s % 10
            carry = s // 10

            curr.next = ListNode(r)
            curr = curr.next

            if not l1:
                l2 = l2.next
            elif not l2:
                l1 = l1.next
            else:
                l1 = l1.next
                l2 = l2.next

        if carry != 0:
            curr.next = ListNode(carry)

        return dummy.next

            

        