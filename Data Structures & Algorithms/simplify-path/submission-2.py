class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []
        cur = ""

        for element in path + '/':
            if element == '/':
                if cur == "..":
                    if stack:
                        stack.pop()

                elif cur != '.' and cur != "":
                    stack.append(cur)

                cur = ""

            else:
                cur += element

        return '/' + '/'.join(stack)


        