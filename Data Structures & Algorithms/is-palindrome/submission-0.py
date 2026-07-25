class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        a = ""
        for i in range(len(s)):
            if(s[i].isalnum()):
                a = a + s[i]

        return a == a[::-1]
        