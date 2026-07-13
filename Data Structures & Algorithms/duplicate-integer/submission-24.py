class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        stack = []

        for i in nums:
            if not stack:
                stack.append(i)
            else:
                if i in stack:
                    return True
                else:
                    stack.append(i)

        return False

        

    

        



        
        
        