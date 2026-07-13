"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        curr = head
        oldtonew = {}

        while curr:
            node = Node(curr.val)
            oldtonew[curr] = node
            curr = curr.next

        # {node1, node2, node3, node4}

        curr = head
        
        while curr:
            oldtonew[curr].next = oldtonew[curr.next] if curr.next else None
            oldtonew[curr].random = oldtonew[curr.random] if curr.random else None
            curr = curr.next

        return oldtonew[head]



        

        
            

        
        