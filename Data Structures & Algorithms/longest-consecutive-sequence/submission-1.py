class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        MaxConsec = 0

        for i in range(len(nums)):
            startingNum = nums[i]

            counter =  0 
            consec = 0

            while((startingNum + counter) in nums):
                counter += 1
                consec += 1

            if(MaxConsec < consec):
                MaxConsec =  consec
                
        return MaxConsec
                

