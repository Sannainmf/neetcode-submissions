class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        dih = {']':'[', ')':'(', '}':'{'} 

        for char in s:
            if char not in dih:
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if dih[char] != popped:
                        return False

        return len(stack) == 0
                



        
        