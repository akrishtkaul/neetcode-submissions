class Solution:
    def countBits(self, n: int) -> List[int]:\

        numbers = list(range(n + 1)) # 5 (0b101 -> 2), 7 (0b111 -> 3), 12 (0b1100 -> 2)
        total_bits = [n.bit_count() for n in numbers]

        return total_bits