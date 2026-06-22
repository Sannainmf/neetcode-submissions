class Solution:
    def calPoints(self, operations: List[str]) -> int:

        """
        lit js apply operations
        """

        res = []
        
        for i in range(len(operations)):
            element = operations[i]
            
            if element == "D":
                res.append(res[-1] * 2)
            elif element == "+":
                res.append(res[-1] + res[-2])
            elif element == "C":
                res.pop()
            else:
                res.append(int(element))

        val = 0
        for num in res:
            val += int(num)

        return val

        






        

        