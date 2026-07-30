class Solution:
    def islandsAndTreasure(self, rooms: List[List[int]]) -> None:

        """
        This is essentially a BFS solution.
        """

        q = deque()
        visit = []

        def addRoom(r, c):
            if r < 0 or r == len(rooms):
                return

            if c < 0 or c == len(rooms[0]):
                return

            if [r, c] in visit:
                return

            if rooms[r][c] == -1:
                return

            q.append([r, c])
            visit.append([r, c])

        for r in range(len(rooms)):
            for c in range(len(rooms[0])):
                if rooms[r][c] == 0:
                    q.append([r, c])
                    visit.append([r, c])

        dist = 0

        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                rooms[r][c] = dist

                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)

            dist += 1
