class TimeMap:

    def __init__(self):

        self.hsh = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.hsh:
            self.hsh[key] = []
        
        self.hsh[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.hsh:
            return ""

        l = 0
        r = len(self.hsh[key]) - 1
        k = ""

        while l <= r:
            middle = (l + r) // 2
            if self.hsh[key][middle][1] <= timestamp:
                k = self.hsh[key][middle][0]
                l = middle + 1
            else:
                r = middle - 1

        return k


        
