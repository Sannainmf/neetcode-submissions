class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:



        start = '0000'

        if start in deadends:
            return -1
        q = deque()
        q.append(start)
        seen = set()
        seen.add(start)
        count = 0

        def add(index, string):
            
            dig = int(string[index])

            addOne = (dig + 1) % 10
            newAdd = string[:index] + str(addOne) + string[index + 1:]
            if newAdd not in deadends and newAdd not in seen:
                q.append(newAdd)
                seen.add(newAdd)
                if newAdd == target:
                    return True

            minusOne = (dig + 9) % 10
            newMinus = string[:index] + str(minusOne) + string[index + 1:]
            if newMinus not in deadends and newMinus not in seen:
                q.append(newMinus)
                seen.add(newMinus)
                if newMinus == target:
                    return True

            return False
            

        while q:

            for i in range(len(q)):
                digit = q.popleft()

                if (add(0, digit[:]) or add(1, digit[:]) or add(2, digit[:]) or add(3, digit[:])):
                    return count + 1

            count += 1

        return -1






                