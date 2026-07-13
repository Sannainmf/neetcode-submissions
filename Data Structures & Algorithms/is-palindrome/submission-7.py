class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = []

        for c in s:
            if c.isalnum():
                result.append(c.lower())

        result = "".join(result)


        if result == result[::-1]:
            return True
        else:
            return False
        