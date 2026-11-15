class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        maxLength = 0
        hm = {}
        l = 0
        r = 0

        while r < len(s):

            if s[r] in hm:
                l = max(l , hm[s[r]] + 1)
            
            maxLength = max(maxLength, r - l + 1)
            
            hm[ s[r] ] = r
            r += 1



        return maxLength
        