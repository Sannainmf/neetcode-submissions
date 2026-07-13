class ListNode:
    def __init__(self, val, next, prev):
        self.val = val
        self.next = next
        self.prev = prev

class MyCircularQueue:

    def __init__(self, k: int):
        self.space = k
        self.size = 0
        self.left = ListNode(-1, None, None)
        self.right = ListNode(-1, None, None)
        self.right.prev = self.left
        self.left.next = self.right
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        node = ListNode(value, None, None)
        t = self.right.prev
        t.next = node
        self.right.prev = node
        node.prev = t
        node.next = self.right
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        self.size -= 1
        return True

    def Front(self) -> int:

        return self.left.next.val
        

    def Rear(self) -> int:

        return self.right.prev.val
        

    def isEmpty(self) -> bool:
        if self.size <= 0:
            return True

        return False
        

    def isFull(self) -> bool:
        if self.size >= self.space:
            return True

        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()