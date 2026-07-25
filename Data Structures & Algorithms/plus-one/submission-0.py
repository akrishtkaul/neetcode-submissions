class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits) - 1
        digits[n] += 1

        while n > 0 and digits[n] == 10:
            digits[n] = 0
            digits[n - 1] += 1
            n -= 1

        if digits[0] == 10:
            digits[0] = 0
            digits.insert(0, 1)

        return digits
            
        