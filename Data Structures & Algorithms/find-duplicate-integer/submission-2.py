class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        h , t = 0, 0

        while True: 
            
            h = nums[nums[h]]
            t = nums[t]

            if h == t:
                break
            
        t2 = 0
        while True:
            t = nums[t]
            t2 = nums[t2]
            if t == t2:
                return t
        