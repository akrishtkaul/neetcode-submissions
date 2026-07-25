class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
   
        hm = {}

        for i in range( len(tasks) ):
            if tasks[i] not in hm.keys():
                hm[tasks[i]] = 1
            else:
                hm[tasks[i]] += 1
        
        taskScheduler = []

        for key in hm.keys():
            heapq.heappush(taskScheduler, -hm[key] )

        queue = deque()

        cycles = 0

        while len(taskScheduler) > 0 or len(queue) > 0:

            if queue and cycles == queue[0][1]:
                freq, _ = queue.popleft()
                heapq.heappush(taskScheduler, freq)

            cycles += 1
            
            if taskScheduler:
                frequency = heapq.heappop(taskScheduler)
                frequency += 1  
                
                if frequency < 0:
                    queue.append( (frequency , cycles + n) )
            else:
                pass
    
        return cycles

        




           
         




        