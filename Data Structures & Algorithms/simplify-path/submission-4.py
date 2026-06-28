class Solution:
    def simplifyPath(self, path: str) -> str:
        
        res = ""
        stack = []

        for element in path + "/":
            if element == "/":
                if res == "..":
                    if stack:
                        stack.pop()

                elif res != "." and res != "":
                    stack.append(res)
                
                res = ""
                
            else:
                res += element

        return "/" + "/".join(stack)

        