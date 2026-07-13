class Solution:
    def isValid(self, s: str) -> bool:

        hash = {'}':'{', ']':'[', ')':'('}
        stack = []

        for i in s:
            if i not in hash:
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if popped != hash[i]:
                        return False

        return not stack
            