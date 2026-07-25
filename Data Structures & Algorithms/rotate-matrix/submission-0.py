class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        coordinates = set()

        for i in range( len(matrix) ):
            for j in range( len(matrix[0]) ):
                if (i , j) in coordinates:
                    continue
                
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

                coordinates.add((i,j))
                coordinates.add((j,i))

        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]

        

        


        