class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        results  = []

        def backtrack(index , path):
            if index > len(nums) - 1:
                return

            if sum(path) == target:
                results.append(path[:])
                return

            if sum(path) > target:
                return

            path.append(nums[index])
            backtrack(index, path)
            path.pop()

            backtrack(index + 1, path)

        
        backtrack(0 , [])
        
        return results

        