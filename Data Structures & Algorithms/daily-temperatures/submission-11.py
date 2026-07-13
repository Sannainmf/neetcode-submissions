class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        """
        n = len(temperatures)
        stack = []
        answer = [0] * n
        """

        n = len(temperatures)
        stack = []
        answer = [0] * n

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stack_t, stack_i = stack.pop()
                answer[stack_i] = i - stack_i
            
            stack.append((t, i))
        
        return answer


        
        