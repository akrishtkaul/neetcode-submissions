class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows = len(grid)
        cols = len(grid[0])
        directions = [(0,1), (1, 0), (0,-1), (-1, 0)]

        coords = deque()

        def neighbors(row, col):
            potential_neighbors = []

            for nr, nc in directions:
                new_row = row + nr
                new_col = col + nc

                if 0 <= new_row < rows and 0 <= new_col < cols:
                    potential_neighbors.append((new_row, new_col)) 

            return potential_neighbors


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    coords.append((row, col))
        
        while coords:

            row, col = coords.popleft()
    
            for nr, nc in neighbors(row, col):
                if grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[row][col] + 1
                    coords.append((nr, nc))





                    

        





