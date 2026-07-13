class Solution:
    def decodeString(self, s: str) -> str:

        stack = []

        for char in s:

            if char != ']':
                stack.append(char)
            else:
                temp = ""
                while stack[-1] != '[':
                    temp = stack.pop() + temp

                stack.pop()

                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                
                for i in range(int(num)):
                    stack.append(temp)


            
        return ''.join(stack)





                




        

            