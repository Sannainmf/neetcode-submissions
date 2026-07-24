class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        """
        if we hit the end, return True

        if we hit another number, return False
        """

        inc = defaultdict(int)
        out = defaultdict(int)

        for i, j in trust:
            out[i] += 1
            inc[j] += 1

        for k in range(1, n + 1):
            if inc[k] == n - 1 and out[k] == 0:
                return k

        return -1
        