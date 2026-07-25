class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        sheep = []
        heapq.heapify(sheep)

        for num in nums:
            heapq.heappush(sheep, num)
            if len(sheep) > k:
                heapq.heappop(sheep)

        return heapq.heappop(sheep)


        