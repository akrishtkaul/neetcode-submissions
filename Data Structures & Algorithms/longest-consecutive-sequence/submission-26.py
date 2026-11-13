class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 0:
            return 0

        hm = defaultdict(int)
        streak = 1

        for i in range( n ):
            hm[ nums[i] ] = 1
    
        for j in range(n - 1, -1, -1):
            newStreak = 1
            number = nums[j]
            if number - 1 not in hm:
                while (number + 1) in hm:
                    newStreak += 1
                    number += 1

            streak = max(newStreak, streak)
     
        return streak
        



        