class ListNode:
    def __init__(self, key = -1, val = -1, next = None):
        self.key = key
        self.val = val
        self.next = next


class MyHashMap:

    """
    somehow use linkedlists?

    hashmap is a linkedlist. For each element in the linked list just check its 
    key, and from that u can determine if it contains or exists.
    """

    def __init__(self):

        """you make a dummy"""
        self.dummy = ListNode()
        
    def put(self, key: int, value: int) -> None:
        self.curr = self.dummy
        self.second = self.dummy
        while self.curr:
            if self.curr.key == key:
                self.curr.val = value
                break
            self.curr = self.curr.next

        if not self.curr:
            while self.second.next:
                self.second = self.second.next
            
            self.second.next = ListNode(key, value)

    def get(self, key: int) -> int:

        self.curr = self.dummy
        while self.curr:
            if self.curr.key == key:
                return self.curr.val
            self.curr = self.curr.next

        if self.curr is None:
            return -1
        

    def remove(self, key: int) -> None:
        
        self.curr = self.dummy
        while self.curr.next:
            if self.curr.next.key == key:
                self.curr.next = self.curr.next.next
                break
            self.curr = self.curr.next
            
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)