class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        """
        absolute value is size, sign represents direction

        if two asteroids meet, smaller explodes. If both
        same size, both explode. Asteroids moving  in same
        direction never meet
        """

        stack = []

        for a in asteroids:
            alive = True

            if not stack:
                stack.append(a)
                alive = False
            else:
                while a < 0 and alive and stack and stack[-1] > 0:
                    if abs(a) == abs(stack[-1]):
                        stack.pop()
                        alive = False
                    elif abs(a) > abs(stack[-1]):
                        stack.pop()
                    else:
                        alive = False
            
                if alive:
                    stack.append(a)

        return stack


                        
            



        