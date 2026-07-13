class ListNode:
    def __init__(self, val, next, prev):
        self.val = val
        self.next = next
        self.prev = prev

class MyCircularQueue:

    """
    use array somehow?
    """

    def __init__(self, k: int):

        self.maxSize = k
        self.currSize = 0
        self.left = ListNode(-1, None, None)
        self.right = ListNode(-1, None, self.left)
        self.left.next = self.right

    def enQueue(self, value: int) -> bool:

        if self.isFull():
            return False

        node = ListNode(value, None, None)
        prev = self.right.prev
        prev.next = node
        self.right.prev = node
        node.prev = prev
        node.next = self.right

        self.currSize += 1
        return True

    def deQueue(self) -> bool:

        if self.isEmpty():
            return False
        
        self.left.next = self.left.next.next
        self.left.next.prev = self.left

        self.currSize -= 1
        return True

    def Front(self) -> int:
        
        if self.isEmpty():
            return -1

        return self.left.next.val

    def Rear(self) -> int:

        if self.isEmpty():
            return -1

        return self.right.prev.val
        
    def isEmpty(self) -> bool:

        if self.currSize <= 0:
            return True
        else:
            return False
        
    def isFull(self) -> bool:

        if self.currSize >= self.maxSize:
            return True
        else:
            return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()