class Solution:
    def isPalindrome(self, s: str) -> bool:

        StringS = ''.join(char.lower() for char in s if char.isalnum())

        if StringS == StringS[::-1]:
            return True
        else:
            return False



        
       


       

        




       
        