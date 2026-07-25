class Solution:
    def countBits(self, n: int) -> List[int]:\

        results = []
        for i in range(0, n + 1):
            n = i
            count = 0
        
        # Core Brian Kernighan's Algorithm
            while n > 0:
                n &= (n - 1)  # Clear the lowest set bit
                count += 1
            
            results.append(count)
        
        return results