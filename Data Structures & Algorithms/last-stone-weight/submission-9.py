class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        

        while len(stones) > 1:
            stones.sort(reverse=True)
            x = stones[0]
            y = stones[1]

            if x == y:
                del stones[stones.index(x)]
                del stones[stones.index(y)]
            elif x < y:
                stones[1] = y - x
                del stones[stones.index(x)]
            else:
                stones[0] = x - y
                del stones[stones.index(y)]

        return max(stones) if len(stones) > 0 else 0