from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False

        hm = defaultdict(str)
        for i in range(len(t)):
            if(s[i] in hm):
                hm[s[i]] += 1
            else:
                hm[s[i]] = 1

        print(hm)

        for i in range(len(s)):
            if(t[i] in hm):
                if(hm[t[i]] == 0):
                    return False
                else:
                    hm[t[i]] -= 1
            else:
                return False
                
        print(hm)
        return True
        
        