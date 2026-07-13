class Solution:
    def isPalindrome(self, s: str) -> bool:

        string = ''.join(char.lower() for char in s if char.isalnum())

        left = 0
        right = len(string) - 1

        for i in range(len(string)):
            if string[left] == string[right]:
                left += 1
                right -= 1
            else:
                return False
        
        return True

      
       


       

        




       
        