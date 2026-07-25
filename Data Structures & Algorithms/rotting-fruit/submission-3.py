class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        def infect(row, col, uldr):
            for direction in uldr:
                r , c = direction
                new_row  = row + r
                new_col  = col + c

                if new_row < 0 or new_row > rows - 1:
                    continue

                if new_col > columns - 1 or new_col < 0:
                    continue

                if grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2
                    coordinates.append((new_row, new_col))


        rows = len(grid)
        columns = len(grid[0])
        coordinates = deque()
        counter = 0

        udlr = [(0,1), (0,-1), (-1,0), (1,0)]

        for row in range(rows):
            for col in range(columns):
                if grid[row][col] == 2:
                    coordinates.append((row, col))  

        while len(coordinates) > 0:
            number_infected = len(coordinates)

            for i in range(number_infected):
                tile_row, tile_column = coordinates.popleft()
                infect(tile_row, tile_column, udlr)
            
            if len(coordinates) > 0:
                counter += 1
            
   
        for row in range(rows):
            for col in range(columns):
                if grid[row][col] == 1:
                    return -1

        
        return counter

            




        