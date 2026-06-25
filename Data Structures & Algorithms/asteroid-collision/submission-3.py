class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        """
        array of asteroids
        indicies represent relative position
        abs val = size
        the sign = direction | + = right | - = left
        all asteroids same velocity

        smaller one explodes
        same size both explodes
        same direction never meet
        """

        stack = []

        for a in asteroids:
            alive = True
            while stack and a < 0 and stack[-1] > 0:
                if abs(a) > abs(stack[-1]):
                    stack.pop()
                elif abs(a) - abs(stack[-1]) == 0:
                    stack.pop()
                    a = 0
                    alive = False
                elif abs(a) < abs(stack[-1]):
                    alive = False
                    a = 0

            if alive:
                stack.append(a)

        return stack