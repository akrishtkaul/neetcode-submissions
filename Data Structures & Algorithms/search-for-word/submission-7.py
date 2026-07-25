class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        columns = len(board[0])

        def dfs(board, row, col, index) -> bool:
            if index > len(word) - 1:
                return True

            if row < 0 or row > rows - 1 or col < 0 or col > columns - 1:
                return False
            
            if board[row][col] == word[index]:
                board[row][col] = "#"
                found = ( dfs(board, row - 1, col, index + 1) 
                or dfs(board, row + 1, col, index + 1) 
                or dfs(board, row, col - 1, index + 1) 
                or dfs(board, row, col + 1, index + 1) )
                board[row][col] = word[index]
                return found

            else:
                return False


        for row in range(rows):

            for col in range(columns):
                if board[row][col] == word[0]:
                    board[row][col] = "#"
                    found = ( dfs(board, row - 1, col, 1) 
                        or dfs(board, row + 1, col, 1)
                        or dfs(board, row, col - 1, 1)
                        or dfs(board, row, col + 1, 1) ) 

                    if found:
                        return found

                    board[row][col] = word[0]
                    
                    


        
        return False

                




        