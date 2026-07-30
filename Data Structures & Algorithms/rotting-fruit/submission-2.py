class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        """
        2 means its rotting, 1 means its normal, 0 means no banana

        this is just a bfs
        """

        q = deque()
        visit = []
        m = 0

        def addFruit(r, c):
            if r < 0 or r == len(grid):
                return

            if c < 0 or c == len(grid[0]):
                return

            if [r, c] in visit:
                return

            if grid[r][c] == 0:
                return

            q.append([r, c])
            visit.append([r, c])
            count[0] -= 1


        count = [0]

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append([r, c])
                    visit.append([r, c])
                
                if grid[r][c] == 1:
                    count[0] += 1

        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                addFruit(r + 1, c)
                addFruit(r - 1, c)
                addFruit(r, c + 1)
                addFruit(r, c - 1)

            if q:
                m += 1

        if count[0] != 0:
            return -1
    

        return m

                
        
        