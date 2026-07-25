class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        seen = [[False] * cols for _ in range(len(grid))]
        

        def findArea(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return 0

            if seen[row][col] or grid[row][col] == 0:
                return 0

            seen[row][col] = True

            return (1
                    + findArea(row + 1, col)
                    + findArea(row - 1, col)
                    + findArea(row, col + 1)
                    + findArea(row, col - 1))

        max_plot = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and not seen[i][j]:
                    max_plot = max(max_plot, findArea(i, j))

        return max_plot
                 

