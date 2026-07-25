class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        combinations = []

        def backtrack(path, openingCount, closingCount):
            if openingCount == n and closingCount == n:
                combinations.append(path)
                return

            if openingCount > n:
                return
            
            if closingCount > openingCount:
                return
            
            backtrack(path + "(", openingCount + 1, closingCount)

            backtrack(path + ")" , openingCount, closingCount + 1)

        
        backtrack("", 0 , 0)

        return combinations







        
