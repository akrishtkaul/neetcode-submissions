class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l = 0 
        r = len(s1) - 1

        while( r < len(s2) ):
            if("".join(sorted(s1)) == "".join(sorted(s2[l:r + 1]))):
                return True
            else:
                r += 1
                l += 1
        
        return False

        
        