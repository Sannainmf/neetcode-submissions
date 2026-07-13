class ListNode:
    def __init__(self, key = -1, val = -1, next = None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):

        self.dummy = ListNode()
        
    def put(self, key: int, value: int) -> None:

        curr = self.dummy
        exists = False

        while curr.next:
            curr = curr.next

            if curr.key == key:
                curr.val = value
                exists = True

        if exists is False:
            curr.next = ListNode(key, value)

    def get(self, key: int) -> int:
        
        curr = self.dummy

        while curr.next:
            curr = curr.next

            if curr.key == key:
                return curr.val
        
        return -1

    def remove(self, key: int) -> None:

        curr = self.dummy

        while curr.next:

            if curr.next.key == key:
                curr.next = curr.next.next
                break
            else:
                curr = curr.next

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)