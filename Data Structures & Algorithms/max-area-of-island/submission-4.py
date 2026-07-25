class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        seen = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        max_plot = 0
        current_plot = 0
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):

            for j in range(cols):

                square = seen[i][j]

                if square:
                    continue

                if grid[i][j] == 1:
                    current_plot = self.findArea(grid, seen, i, j)
                
                max_plot = max(max_plot, current_plot)
                current_plot = 0
        
        return max_plot

    
    def findArea(self, grid:List[List[int]], seen: List[List[bool]], row, col) -> int:
        if row < 0 or row > len(grid) - 1 or col < 0 or col > len(grid[0]) - 1:
            return 0

        if seen[row][col]:
            return 0

        seen[row][col] = True

        if grid[row][col] == 0:
            return 0
        
        return 1 + self.findArea(grid, seen, row + 1, col) + self.findArea(grid, seen, row - 1, col) + self.findArea(grid, seen, row, col + 1) + self.findArea(grid, seen, row, col - 1)
                 




        
     

        