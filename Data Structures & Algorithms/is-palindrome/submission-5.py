class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = []

        for c in s:
            if c.isalnum():
                result.append(c)

        result = "".join(result)

        result = result.lower()

        if result == result[::-1]:
            return True
        else:
            return False
        