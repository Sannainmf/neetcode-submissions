class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:


        string = '0000'

        if string in deadends:
            return -1
            
        seen = set()
        seen.add(string)
        q = deque()
        q.append(string)
        cost = 0

        def add(idx, s):
            digit = int(s[idx])

            add = (digit + 1) % 10
            addS = s[:idx] + str(add) + s[idx + 1:]
            if addS not in seen and addS not in deadends:
                seen.add(addS)
                q.append(addS)
                if addS == target:
                    return True

            minus = (digit + 9) % 10
            minusS = s[:idx] + str(minus) + s[idx + 1:]
            if minusS not in seen and minusS not in deadends:
                seen.add(minusS)
                q.append(minusS)
                if minusS == target:
                    return True

            return False

        while q:
            for i in range(len(q)):
                num = q.popleft()

                if add(0, num[:]) or add(1, num[:]) or add(2, num[:]) or add(3, num[:]):
                    return cost + 1

            cost += 1

        return -1
        