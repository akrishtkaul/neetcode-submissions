class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        index = len(nums) - 1  # scanning pointer
        goal = len(nums) - 1    # leftmost provably-good index

        while index > 0:
            if index - 1 + nums[index - 1] >= goal:
                goal = index - 1
            index -= 1  # always decrement, regardless

        return goal == 0

