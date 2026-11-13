class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        majority = len(nums) / 3
        hm = defaultdict(int)
        majorityElement = []

        for num in nums:
            hm[num] += 1

        for key in hm.keys():
            if hm[key] > majority:
                majorityElement.append(key)
        
        return majorityElement

        
 
