class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        arr = []

        for i in nums:
            if not arr:
                arr.append(i)
            else:
                if i in arr:
                    return True
                else:
                    arr.append(i)
        
        return False

        

    

        



        
        
        