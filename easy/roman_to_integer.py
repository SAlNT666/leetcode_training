# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def __init__(self):
        self.digits = dict(zip(('I', 'V', 'X', 'L', 'C', 'D', 'M'), (1, 5, 10, 50, 100, 500, 1000)))

    def romanToInt(self, s: str) -> int:
        res = 0

        for i, d in enumerate(s):
            if i > 0 and self.digits[d] > self.digits[s[i - 1]]:
                res += self.digits[d] - 2 * self.digits[s[i - 1]]
            else:
                res += self.digits[d]
        return res


S = Solution()
romanToInt = S.romanToInt
print(romanToInt('III'), 3)
print(romanToInt('LVIII'), 58)
print(romanToInt('MCMXCIV'), 1994)
