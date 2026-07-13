class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        result = set()

        for num in nums:
            result.add(num)


        if len(result) == len(nums):
            return False
    
        return True
        

    

        



        
        
        