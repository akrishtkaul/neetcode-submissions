class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in board:
            hm = defaultdict(int) 
            for number in row:
                if number == ".":
                    continue
                if number in hm.keys():
                    print("returning False at row" , number )

                    return False
                hm[number] += 1

        for i in range(9):
            hm = defaultdict(int)
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in hm.keys():
                    return False
                hm[board[j][i]] += 1
        
        boxes = defaultdict(set)

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                    
                box_key = (i // 3, j // 3)
                if num in boxes[box_key]:
                    return False
                boxes[box_key].add(num)
        

        return True