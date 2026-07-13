class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        """
        compare first element num2 with nums1. When u get to a number where num1
        element is greater than nums2, shift everything including nums 1 element down 1 in the array.
        and insert nums2 element. Repeat with next nums 2 element
        
        *3 pointers:
            one is left, one is start (where nums > nums2),  and one is end (end of nums1).

            you find the condition, and then you swap

            
        """

        last = m + n - 1

        while m > 0 and n > 0:
            if nums2[n - 1] > nums1[m - 1]:
                nums1[last] = nums2[n - 1]
                last -= 1
                n -= 1
            else:
                nums1[last] = nums1[m - 1]
                last -= 1
                m -= 1

        while n > 0:
            nums1[last] = nums2[n - 1]
            last -= 1
            n -= 1

             



        





        