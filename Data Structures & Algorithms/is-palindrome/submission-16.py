class Solution:
    def isPalindrome(self, s: str) -> bool:

        correctS = ''.join(char.lower() for char in s if char.isalnum())

        if correctS == correctS[::-1]:
            return True
        else:
            return False


        
       


       

        




       
        