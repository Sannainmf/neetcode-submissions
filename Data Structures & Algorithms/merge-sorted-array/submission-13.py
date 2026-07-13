class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        """
        we need an end pointer, an and of nums1 an end of nums2.
        If nunms2 end greater than nums2 end, nums2 last replace with
        """

        last = m + n - 1

        while m > 0 and n > 0:
            if nums2[n - 1] > nums1[m - 1]:
                nums1[last] = nums2[n - 1]
                n -= 1
            else:
                nums1[last] = nums1[m - 1]
                m -= 1

            last -= 1

        while n > 0:
            nums1[last] = nums2[n - 1]
            last -= 1
            n -= 1
        
        


        