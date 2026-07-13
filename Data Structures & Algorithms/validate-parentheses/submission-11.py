class Solution:
    def isValid(self, s: str) -> bool:

        hash = {'}':'{', ')':'(', ']':'['}
        stack = []

        for char in s:
            if char not in hash:
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if popped != hash[char]:
                        return False
        
        return len(stack) == 0

