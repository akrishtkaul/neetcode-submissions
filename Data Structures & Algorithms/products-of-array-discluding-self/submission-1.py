class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        output = [1] * n
        
        # Calculate exclusive prefix products
        product = 1
        for i in range(n):
            prefix[i] = product
            product *= nums[i]
            
        # Calculate exclusive suffix products
        product = 1
        for j in range(n - 1, -1, -1):
            suffix[j] = product
            product *= nums[j]

        for k in range(n):
            output[k] = prefix[k] * suffix[k]
            
        return output
            

            


        