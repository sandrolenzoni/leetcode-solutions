class Solution(object):
    def reverse(self, x: int) -> int:
        string = str(x)[::-1] if not x < 0 else str(x)[:0:-1]
        if x < -2**31 or int(string) > 2**31 -1:
            return 0 
        return f"-{int(string)}" if x < 0 else int(string)


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverse(-123))



## THE BEST CODE 

# Constants at module level, computed once
INT_MIN = -2**31
INT_MAX = 2**31 - 1

class Solution:
    def reverse(self, x):
        """
        Reverse digits of a 32-bit signed integer in-place with O(1) extra space.
        Return 0 on overflow.
        """
        res = 0
        sign = 1 if x >= 0 else -1
        x = x * sign

        # Process digits without additional data structures
        while x:
            x, digit = divmod(x, 10)
            # Overflow check: only O(1) temporary vars
            if res > INT_MAX // 10 or (res == INT_MAX // 10 and digit > INT_MAX % 10):
                return 0
            res = res * 10 + digit