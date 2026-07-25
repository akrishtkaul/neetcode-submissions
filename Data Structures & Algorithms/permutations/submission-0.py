class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        results = []

        def backtrack(path, remainingList):
            if len(remainingList) == 0:
                results.append(path[:])
                return

            for i in range(len(remainingList)):
                path.append(remainingList[i])
                backtrack(path , remainingList[0 : i] + remainingList[i + 1:])
                path.pop()

        backtrack([], nums)

        return results



