class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        l = 0
        r = 1
        arr = []

        while l < len(temperatures):
            if r == len(temperatures):
                arr.append(0)
                l += 1
                r = l + 1
            elif temperatures[r] > temperatures[l]:
                arr.append(r - l)
                l += 1
                r = l + 1
            else:
                r += 1

        return arr

        # [1, ]




        
        