class Solution:
    def isValid(self, s: str) -> bool:
        openingBrackets = ['{', '[', '(']
        closingBrackets = ['}', ']', ')'] 
        stack = []
        for i in range(len(s)):
            if(s[i] in closingBrackets and len(stack) == 0):
                return False
            if(s[i] in openingBrackets): 
                stack.append(s[i])
            elif((s[i] == ']' and stack[-1] == '[') or (s[i] == ')' and stack[-1] == '(') or (s[i] == '}' and stack[-1] == '{')):
                stack.pop(-1)
            else:
                return False
        if(len(stack) > 0):
            return False
        return True
