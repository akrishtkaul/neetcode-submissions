class Solution:
    def rob(self, nums: List[int]) -> int:
        nums.insert(0,0)
        nums.insert(0,0)

        for i in range(2, len(nums)):
            if(nums[i-1] < nums[i-2] + nums[i]):
                nums[i] = nums[i-2] + nums[i]
            else:
                nums[i] = nums[i-1]
        
        return nums[-1]
        