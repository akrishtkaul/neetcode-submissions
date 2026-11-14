class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        solutions = []

        for i in range( len(nums) ):
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]

                if currentSum == 0:
                    solutions.append([nums[i], nums[left], nums[right]])
                   
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right + 1] == nums[right]:
                        right -= 1
                
                elif currentSum > 0:
                    right -= 1
                
                elif currentSum < 0:
                    left += 1
            


        return solutions

                

                
                


        

       
        