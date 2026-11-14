class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.summedMatrix = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]    
        for r in range(1, len(self.summedMatrix)):

            for c in range(1, len(self.summedMatrix[0])):

                self.summedMatrix[r][c] = (self.summedMatrix[r - 1][c] + self.summedMatrix[r][c - 1]) - self.summedMatrix[r - 1][c - 1] + self.matrix[r - 1][c - 1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        P = self.summedMatrix
        return (
            P[row2 + 1][col2 + 1]
            - P[row1][col2 + 1]
            - P[row2 + 1][col1]
            + P[row1][col1]
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)