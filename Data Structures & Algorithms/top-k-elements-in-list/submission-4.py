class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hm = defaultdict(int)
        for num in nums:
            hm[num] += 1
        
        heap = [(-value, key) for key, value in hm.items()]
        
        heapq.heapify(heap) 
        
        return [heapq.heappop(heap)[1] for _ in range(k)]

            

        