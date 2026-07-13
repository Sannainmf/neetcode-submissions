class MyHashSet:

    def __init__(self):
        self.hshSet = []
        
    def add(self, key: int) -> None:

        if key not in self.hshSet:
            self.hshSet.append(key)
                
    def remove(self, key: int) -> None:
       
        if key in self.hshSet:
            idx = self.hshSet.index(key)
            del self.hshSet[idx]
        
    def contains(self, key: int) -> bool:

        if key in self.hshSet:
            return True
        else:
            return False


        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)