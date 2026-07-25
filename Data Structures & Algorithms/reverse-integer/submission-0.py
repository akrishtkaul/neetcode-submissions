class Solution:
    def reverse(self, x: int) -> int:
        
        copy = abs(x)
        reversedNum = 0

        for i in range(len(str(copy)) - 1, -1, -1):
            digit_x = copy % 10
            reversedNum = reversedNum + ( digit_x * (10 ** i) )
            copy //= 10

        if reversedNum > 2**31 - 1 or reversedNum < -2**31:
            return 0

        return -reversedNum if x < 0 else reversedNum
