class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+" , "/", "-" , "*"]

        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                nums2 = stack.pop()
                nums1 = stack.pop()
                if t == "+":
                    answer = nums1 + nums2
                elif t == "-":
                    answer = nums1 - nums2
                elif t == "*":
                    answer = nums1 * nums2
                elif t == "/":
                    answer = int(nums1 / nums2)
            
                stack.append(answer)
        
        return stack[-1]

        