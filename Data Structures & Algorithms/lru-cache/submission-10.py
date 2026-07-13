class ListNode:
    def __init__(self, key, val, next, prev):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def getInsert(self, node):
        """
        gets fed in node ur trying to insert
        """

        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

        t = self.right.prev
        t.next = node
        self.right.prev = node
        node.prev = t
        node.next = self.right

    def putInsert(self, node):

        t = self.right.prev
        t.next = node
        self.right.prev = node
        node.prev = t
        node.next = self.right

    def delete(self, node):

        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def __init__(self, capacity: int):

        self.cap = capacity
        self.hsh = {}
        self.space = 0
        self.left = ListNode(-1, -1, None, None)
        self.right = ListNode(-1, -1, None, self.left)
        self.left.next = self.right
        
    def get(self, key: int) -> int:

        if key in self.hsh:
            self.getInsert(self.hsh[key])
            return self.hsh[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if key in self.hsh:
            self.hsh[key].val = value
            self.getInsert(self.hsh[key])
        else:
            node = ListNode(key, value, None, None)
            self.hsh[key] = node
            self.putInsert(self.hsh[key])
            self.space += 1

        if self.space > self.cap:
            node = self.left.next
            self.delete(self.hsh[node.key])
            del self.hsh[node.key]
            self.space -= 1
            
        
