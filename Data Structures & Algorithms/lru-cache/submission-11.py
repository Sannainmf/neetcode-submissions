class ListNode:
    def __init__(self, key, val, next, prev):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def insert(self, node):

        nxt = self.right
        prev = self.right.prev
        prev.next = node
        node.next = nxt
        nxt.prev = node
        node.prev = prev


    def delete(self, node):

        nxt = node.next
        prev = node.prev
        prev.next = nxt
        nxt.prev = prev


    def __init__(self, capacity: int):

        self.cap = capacity
        self.currSize = 0
        self.hsh = {}
        self.left = ListNode(-1, -1, None, None)
        self.right = ListNode(-1, -1, None, self.left)
        
    def get(self, key: int) -> int:

        if key in self.hsh:
            node = self.hsh[key]
            self.delete(node)
            self.insert(node)
            return self.hsh[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:

        if key not in self.hsh:
            node = ListNode(key, value, None, None)
            self.hsh[key] = node
            self.insert(self.hsh[key])
            self.currSize += 1
        else:
            node = ListNode(key, value, None, None)
            self.delete(self.hsh[key])
            self.hsh[key] = node
            self.insert(self.hsh[key])

        if self.currSize > self.cap:
            node = self.left.next
            self.delete(self.hsh[node.key])
            del self.hsh[node.key]
            self.currSize -= 1



            




        