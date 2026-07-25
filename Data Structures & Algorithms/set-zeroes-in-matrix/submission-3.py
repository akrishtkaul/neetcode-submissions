class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        rows = len(matrix)
        columns = len(matrix[0])
        

        for i in range( rows ):
            for j in range( columns ):

                if matrix[i][j] == 0:

                    for row in range(rows):
                        if matrix[row][j] == 0:
                            continue
                        matrix[row][j] = "#"

                    for column in range(columns):
                        if matrix[i][column] == 0:
                            continue
                        matrix[i][column] = "#"

        
        for i in range( rows ):
            for j in range( columns ):
                if matrix[i][j] == "#":
                    matrix[i][j] = 0

                
        