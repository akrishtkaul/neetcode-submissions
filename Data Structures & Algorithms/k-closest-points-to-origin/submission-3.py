class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        kClosestPoints = []
        heapq.heapify(kClosestPoints)

        for point in points:
            distance = math.sqrt((point[0] - 0) * (point[0] - 0) + (point[1] - 0) * (point[1] - 0))

            heapq.heappush(kClosestPoints, (distance, point))
        
        return [heapq.heappop(kClosestPoints)[1] for _ in range(k)]

        

        