class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        prev2, prev1 = 0, 0 
        for i in range(len(nums)-1):
            prev2, prev1 = prev1, max(prev1, prev2 + nums[i])

        prev4, prev3 = 0, 0 
        for j in range(1,len(nums)):
            prev4, prev3 = prev3, max(prev3, prev4 + nums[j])
        
        return max(prev3,prev1)


        