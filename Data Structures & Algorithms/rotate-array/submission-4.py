class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)

        def rotateHelper(leftIndex, rightIndex):
            while leftIndex < rightIndex:
                nums[rightIndex] , nums[leftIndex] = nums[leftIndex] , nums[rightIndex]
                leftIndex += 1
                rightIndex -= 1
 
        
        rotateHelper(0, len(nums) - 1)
        rotateHelper(0, k - 1)
        rotateHelper(k, len(nums) - 1)


        
    