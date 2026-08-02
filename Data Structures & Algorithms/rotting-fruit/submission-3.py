class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        q = deque()
        seen = []
        count = 0
        bCount = [0]
        sCount = 0

        def add(r, c):
            if r < 0 or r == len(grid):
                return

            if c < 0 or c == len(grid[0]):
                return

            if grid[r][c] == 0:
                return

            if [r, c] in seen:
                return

            q.append([r, c])
            seen.append([r, c])
            bCount[0] += 1
        

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append([i, j])
                    seen.append([i, j])
                elif grid[i][j] == 1:
                    sCount += 1

        while q:

            for i in range(len(q)):
                r, c = q.popleft()

                add(r + 1, c)
                add(r - 1, c)
                add(r, c + 1)
                add(r, c - 1)

            if q:
                count += 1

        if bCount[0] == sCount:
            return count
        else:
            return -1
            
        """ 
        i guess we  can also count how many 1s, and as were adding, we increment another var, we check if
        equal, if equal we return count, if not return -1
        """


                

        