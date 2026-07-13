class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        """
        position[i] is pos of ith car
        speed[i] is speed of ith car

        destination is position target

        a car cannot pass another car ahead of  it. It can 
        catch up to another car qnd drive the same speed as
        the car ahead of it.

        A car fleet is a set of cars driving at same position
        and same speed. Single car is a fleet too
        """

        """
        looping backards, calculate the time for the last most.
        if car behind it has a time less than or equal to that,
        it forms a fleet. 
        """

        z = sorted(zip(position, speed))
        stack = []

        for p, s in z[::-1]:
            t = (target - p) / s

            if not stack:
                stack.append(t)
            elif t > stack[-1]:
                stack.append(t)
        
        return len(stack)


        