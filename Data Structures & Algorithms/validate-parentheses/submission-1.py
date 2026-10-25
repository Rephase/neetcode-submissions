class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')':'(',
                '}':'{',
                ']':'['}


        for char in s:
            if char in '({[':
                stack.append(char)
            elif not stack:
                return False
            elif stack[-1] == pairs[char]:
                stack.pop()
            else:
                return False
        
        return not stack