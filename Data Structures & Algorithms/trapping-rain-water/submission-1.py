class Solution:
    def trap(self, height: List[int]) -> int:
        Lwall = Rwall = 0
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n

        for i in range(n):
            j = -i -1
            max_left[i] = Lwall
            max_right[j] = Rwall
            Lwall = max(Lwall, height[i])
            Rwall = max(Rwall, height[j])

        summ = 0
        for i in range(n):
            pot = min(max_left[i], max_right[i])
            summ += max(0, pot - height[i])

        return summ

        
        