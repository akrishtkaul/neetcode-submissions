class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hm = defaultdict(int)

        for i in range( len(nums) ):
            hm[nums[i]] += 1

        heap = []

        for key,value in hm.items():

            heapq.heappush(heap, (-value, key))

        print(heap)

        counter = 0
        kfrequent = []
        while len(heap) > 0 and counter < k:
            kfrequent.append(heapq.heappop(heap)[1])
            counter += 1
        
        return kfrequent

            

        