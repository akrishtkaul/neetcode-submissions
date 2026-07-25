class Solution:
    def reverseBits(self, n: int) -> int:

        new_num = 0
        
        for i in range(31, -1, -1):
            
            new_num = new_num | ( (n & 1) << i)

            n = n >> 1



        return new_num