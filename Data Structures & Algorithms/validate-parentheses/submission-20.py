class Solution:
    def isValid(self, s: str) -> bool:
        
        hashmap = {"]" : "[", ")" : "(", "}" : "{"}
        stack = []

        for char in s:
            if char not in hashmap:
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    element = hashmap[char]
                    if popped != element:
                        return False
                    

        return len(stack) == 0
            
                
