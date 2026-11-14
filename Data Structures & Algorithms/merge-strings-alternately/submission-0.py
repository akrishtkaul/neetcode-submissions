class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        l = 0
        r = 0

        final = ''

        while l < len(word1) and r < len(word2):

            final = final + word1[l] + word2[r]
            
            l += 1
            r += 1

        print(final)
        
        if len(word1) > len(word2):
            return final + word1[l:]

        return final + word2[r:]

