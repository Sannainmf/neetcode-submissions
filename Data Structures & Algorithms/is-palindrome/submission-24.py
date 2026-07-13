class Solution:
    def isPalindrome(self, s: str) -> bool:

        conditions = ''.join(char.lower() for char in s if char.isalnum())

        if conditions == conditions[::-1]:
            return True
        else:
            return False



      
       


       

        




       
        