class Solution:
    def partition(self, s: str) -> List[List[str]]:

        combinations = []

        def backtrack(index, path):
            if index == len(s):
                combinations.append(list(path))
                return

            for i in range(index + 1, len(s) + 1):
                currentString = s[index : i]

                if currentString == currentString[::-1]:
                    path.append(currentString)
                    backtrack(i , path)
                    path.pop()


        backtrack(0 , [])

        return combinations
         
                
        



        

    
        