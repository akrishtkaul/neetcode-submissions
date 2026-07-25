class Solution:
    def missingNumber(self, nums: List[int]) -> int:
       
        xor_sum = 0
       
        for num in range(len(nums) + 1):
            xor_sum ^= num
        
        for num in nums:
            xor_sum ^= num

        return xor_sum



        