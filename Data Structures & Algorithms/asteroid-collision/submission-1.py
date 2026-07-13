class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for a in asteroids:
            alive = True
            if not stack:
                stack.append(a)
            else:
                while stack and a < 0 and stack[-1] > 0:
                    right = abs(a)
                    left = abs(stack[-1])

                    if right > left:
                        stack.pop()
                    elif right - left == 0:
                        stack.pop()
                        a = 0
                        alive = False
                    elif right < left:
                        a = 0
                        alive = False
                        
                if alive:
                    stack.append(a)

        return stack



                    


        