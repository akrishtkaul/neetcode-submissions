class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        hm = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        combinations = []

        def backtrack(index, path):
            if index == len(digits):
                combinations.append(path)
                return    
            
            for letter in hm[ digits[index] ]:
       
                backtrack(index + 1 , path + letter )
                
        if len(digits) == 0:
            return combinations
        backtrack( 0 , "" )

        return combinations

            


        