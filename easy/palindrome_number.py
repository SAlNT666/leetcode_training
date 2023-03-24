# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            n = x
            reversed_x = 0
            while n:
                reversed_x = reversed_x * 10 + n % 10
                n = n // 10
            return x == reversed_x


S = Solution()
isPalindrome = S.isPalindrome
print(isPalindrome(121), True)
print(isPalindrome(0), True)
