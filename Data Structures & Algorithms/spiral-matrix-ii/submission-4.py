class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:


        up , down = 0 , n - 1 
        left , right = 0, n - 1
        counter = 1

        matrix = [[0] * n for i in range(n)]

        while left <= right and up <= down:

            for i in range(left, right + 1):
                matrix[up][i] = counter
                counter += 1
            up += 1

            for j in range(up, down + 1):
                matrix[j][right] = counter
                counter += 1
            right -= 1

            for k in range(right, left - 1, -1):
                matrix[down][k] = counter
                counter += 1
            down -= 1

            for l in range(down, up - 1, -1):
                matrix[l][left] = counter
                counter += 1
            left += 1

        return matrix
            


        