class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
    
        frequentChars = {}
        l , r , length = 0 , 0 , 0

        while (r < len(s)):
            if(s[r] in frequentChars.keys()):
                frequentChars[s[r]] += 1
            else:
                frequentChars[s[r]] = 1

            if(k >= (r + 1 - l) - max(frequentChars.values())):
                r += 1
            else:
                while(k < (r + 1 - l) - max(frequentChars.values())):
                    frequentChars[s[l]] -= 1
                    l += 1
                r += 1
                
            if(length < r - l):
                length = r - l
        
        return length


        

        