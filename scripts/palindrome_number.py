class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]



## LEET CODE BEST SOLUTION

class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = str(x)
        reversed = original[::-1]
        return original == reversed