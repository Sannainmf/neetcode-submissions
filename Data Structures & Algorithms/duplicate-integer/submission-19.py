class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        stack = []

        for num in nums:
            if not stack:
                stack.append(num)
            else:
                if num in stack:
                    return True
                else:
                    stack.append(num)
                
        return False
            


        

        

    

        



        
        
        