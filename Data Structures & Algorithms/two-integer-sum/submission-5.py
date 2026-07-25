class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = defaultdict(int)

        for i in range(len(nums)):
            hm[nums[i]] = i

        difference = 0
        for j in range(len(nums)):
            difference = target - nums[j]
            if(difference in hm and j != hm[difference]):
                if(j > hm[difference]):
                    return [hm[difference], j]
                else:
                    return [j, hm[difference]]

        



        