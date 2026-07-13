class Solution:
    def isPalindrome(self, s: str) -> bool:

        string = ''.join(char.lower() for char in s if char.isalnum())

        if string == string[::-1]:
            return True
        else:
            return False

            
       
        