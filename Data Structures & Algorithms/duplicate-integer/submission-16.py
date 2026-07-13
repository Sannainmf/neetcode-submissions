class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        for i in range(len(nums)):
            curValue = nums[i]
            for j in range(i + 1, len(nums)):
                if curValue == nums[j]:
                    return True
                
        return False
            


        

        

    

        



        
        
        