class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        res = 0
        stack = []

        for element in tokens:
            if element == "+":
                res = stack.pop() + stack.pop()
                stack.append(res)
            elif element == "-":
                a = stack.pop()
                b = stack.pop()
                res = b - a
                stack.append(res)
            elif element == "*":
                res = stack.pop() * stack.pop()
                stack.append(res)
            elif element == "/":
                a = stack.pop()
                b = stack.pop()
                res = int(b / a)
                stack.append(res)
            else:
                stack.append(int(element))

        return stack[-1]





        