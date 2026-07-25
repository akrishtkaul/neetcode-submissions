class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    
        l , r = 0 , 0
        maxLen = 0

        while(r < len(s)):
            if(s[r] in s[l:r]):
                l = l + s[l:r].index(s[r]) + 1
            else:
                r += 1
            if(maxLen < r - l):
                maxLen = r - l


        return maxLen 
            