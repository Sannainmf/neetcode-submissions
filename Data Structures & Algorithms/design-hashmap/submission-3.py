class listNode:
    def __init__(self, key = -1, val = -1, next = None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):

        self.hshMap = {}
        
    def put(self, key: int, value: int) -> None:

        if key in self.hshMap:
            self.hshMap[key].val = value
        else:
            self.hshMap[key] = listNode(key, value)

              

    def get(self, key: int) -> int:

        if key in self.hshMap:
            return self.hshMap[key].val
        else:
            return -1
        

    def remove(self, key: int) -> None:
        if key in self.hshMap:
            del self.hshMap[key]

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)