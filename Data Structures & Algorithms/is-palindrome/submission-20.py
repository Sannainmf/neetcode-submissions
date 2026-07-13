class Solution:
    def isPalindrome(self, s: str) -> bool:

        stringS = ''.join(char.lower() for char in s if char.isalnum())

        if stringS == stringS[::-1]:
            return True
        else:
            return False


        
       


       

        




       
        