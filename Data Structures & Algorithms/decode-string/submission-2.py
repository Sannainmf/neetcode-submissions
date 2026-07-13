class Solution:
    def decodeString(self, s: str) -> str:

        """
        append everything to a stack as you go thru it
        once you hit ], pop the stack until u hit [,
        while loop till u hit a non integer,
        loop append to the stack
        """

        stack = []

        for element in s:
            
            if element != ']':
                stack.append(element)
            else:
                s = ""
                while stack and stack[-1] != '[':
                    s = stack.pop() + s
                
                stack.pop()

                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                for i in range(int(num)):
                    stack.append(s)

        return ''.join(stack)


        