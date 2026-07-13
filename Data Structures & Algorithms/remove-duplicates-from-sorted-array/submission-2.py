class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        """
        so we can have a counter init at zero.

        we can have 2 pointers starting from the beginning, we can just 
        say theyre left and right. We take the elmenet at left (right will be
        indexed 1 more than left at the beginning - every time num at left and right is diff
        we increment counter, and we move l to r. When theyre the same, we dont incrmeent right 
        and remove the current element)
        """

        if not nums:
            return 0

        counter = 0
        p1 = 0
        p2 = 1

        while True:

            if p2 >= len(nums):
                return counter + 1

            if nums[p1] == nums[p2]:
                del nums[p2]
            else:
                counter += 1
                p1 += 1
                p2 += 1
                

            




        