class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        """this is lit just twosum"""

        for i in range(len(numbers)):
            complement = target - numbers[i]
            for j in range(i + 1, len(numbers)):
                if numbers[j] == complement:
                    return [i + 1, j + 1]
                        
                    