class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        """
        sorted int array

        two integer k and x, return k closed integer to x in the array
        result sorted in ascending order

        start at 2 (l), find difference, store in an array. So k = 1
        then go to next num (increment r), find diff, store in array. 
        Now k = 2. When k is max, you can start removing, so increment r,
        if difference less than difference of first one ini array, remove
        first, add r.
        """

        l = 0
        r = 0
        
        while r < len(arr):
            
            if r - l < k:
                r += 1
            else:
                if arr[r] == arr[l]:
                    l += 1
                    r += 1
                elif abs(arr[r] - x) < abs(arr[l] - x):
                    l += 1
                    r += 1
                else:
                    return arr[l : r]

        return arr[l : r]




            
                    
            

     

        

        



        