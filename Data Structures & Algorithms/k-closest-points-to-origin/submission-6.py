class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        kP = []
        heapq.heapify_max(kP)

        for point in points:
            distance = point[0]**2 + point[1]**2
            heapq.heappush_max(kP, (distance, point))

            if len(kP) > k:
                heapq.heappop_max(kP)   # evicts farthest

        return [p for (d, p) in kP]