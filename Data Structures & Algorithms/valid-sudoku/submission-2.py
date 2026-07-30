class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        columns = defaultdict(set)
        box = defaultdict(set)

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue

                box_key = ( i // 3 , j // 3 ) 
                if num in rows[i] or num in columns[j] or num in box[box_key]:
                    return False
                
                rows[i].add(num)
                columns[j].add(num)
                box[box_key].add(num)

        return True






                
               
