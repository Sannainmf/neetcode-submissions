class Solution:
    def isPathCrossing(self, path: str) -> bool:

        arr = []
        coord = [0,0]
        arr.append(coord)

        for i in range(len(path)):
            new = arr[-1][:]
            if path[i] == 'N':
                new[1] += 1
            elif path[i] == 'E':
                new[0] += 1
            elif path[i] == 'S':
                new[1] -= 1
            elif path[i] == 'W':
                new[0] -= 1
            
            if new in arr:
                return True
            else:
                arr.append(new)

        return False
            


        