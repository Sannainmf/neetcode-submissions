class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        arr = []

        for i in range(len(temperatures)):
            if i == len(temperatures) - 1:
                arr.append(0)
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    arr.append(j - i)
                    break
                elif j == len(temperatures) - 1:
                    arr.append(0)

        return arr                    


        