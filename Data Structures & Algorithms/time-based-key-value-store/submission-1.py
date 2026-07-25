class TimeMap:

    def __init__(self):
        self.hm = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hm[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        
        timestamps = [item[0] for item in self.hm[key]]
        if len(timestamps) == 0:
            return ""
        low = 0
        high = len(timestamps) - 1

        while low < high:
            mid = low + (high - low + 1) // 2
    
            if timestamps[mid] <= timestamp:
                low = mid
            else:
                high = mid - 1
                
        if timestamps[low] <= timestamp:
            return self.hm[key][low][1]
        
        return ""

        
