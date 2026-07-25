class Solution:
    def isHappy(self, n: int) -> bool:
        hm = {}

        ans = self.isHappyHelper(n)

        while ans != 1:
            if ans in hm.keys():
                return False
            else:
                hm[ans] = 0

            ans = self.isHappyHelper(ans)

        return True

            
        





    def isHappyHelper(self, n: int) -> int:

        theSum = 0
        while n:
            theSum = theSum + (n % 10) ** 2
            n //= 10

        return theSum



        
        