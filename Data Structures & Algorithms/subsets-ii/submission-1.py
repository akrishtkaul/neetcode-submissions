class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        results = []
        nums.sort()

        def backtrack(index, path):

            if index > len(nums) - 1:
                if path in results:
                    return
                results.append(path[:])
                return

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

            backtrack(index + 1, path)
        
        backtrack(0, [])
        return results
        