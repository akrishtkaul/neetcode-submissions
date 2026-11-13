class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        total = 0
        hm = defaultdict(int)

        hm[0] = 1

        curr_sum = 0

        for i in range( len(nums) ):

            curr_sum += nums[i]

            if curr_sum - k in hm:
                total += hm[curr_sum - k ]
            
            hm[ curr_sum ] += 1
                     
        return total




                
            



        