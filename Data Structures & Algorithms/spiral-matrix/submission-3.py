class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        output = []
        row = 0 
        column = 0

        for i in range( len(matrix[0]) * len(matrix) ):
            output.append(matrix[row][column])
         
            matrix[row][column] = "#"

            if row - 1 >= 0 and matrix[row - 1][column] != "#" and column + 1 < len(matrix[0]) and matrix[row][column + 1] != "#":
                row -= 1
                continue
            if column + 1 < len(matrix[0]) and matrix[row][column + 1] != "#":
                column += 1
                continue
            if row + 1 < len(matrix) and matrix[row + 1][column] != "#":
                row += 1
                continue
            if column - 1 >= 0 and matrix[row][column - 1] != "#":
                column -= 1
                continue
            if row - 1 >= 0 and matrix[row - 1][column] != "#":
                row -= 1
                continue
        
        return output


        