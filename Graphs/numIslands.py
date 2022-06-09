import collections

class Solution:
    def numsIslands(self, grid):
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r,c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))

            while q:
                #bfs
                row, col = q.popleft()
                #dfs
                #row, col = q.pop()
                directions = [[1,0], [-1,0], [0,1], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == "1" and
                        (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r,c)
                    islands += 1
        return islands

if __name__ == '__main__':
    s = Solution()
    grid = [
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "1"]
    ]
    print(s.numsIslands(grid))