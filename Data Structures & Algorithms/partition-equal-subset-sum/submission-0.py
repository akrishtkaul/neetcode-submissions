class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if(sum(nums) % 2 == 1):
            return False
      
        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) -1 ,-1,-1):
            nextdp = set()
            for x in dp:
                if(x + nums[i] == target):
                    return True
                nextdp.add(x+nums[i])
                nextdp.add(x)
            dp.update(nextdp)
        
        return (target in dp)

        

        