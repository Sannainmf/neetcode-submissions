class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        z = sorted(zip(position, speed))
        stack = []

        for p, s in z[::-1]:
            t = (target - p) / s

            if not stack:
                stack.append(t)
            else:
                if stack[-1] < t:
                    stack.append(t)

        return len(stack)
        