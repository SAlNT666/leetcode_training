# https://leetcode.com/problems/integer-to-roman/

class Solution:
    def __init__(self):
        self.digits = dict(zip((1000, 900,  500, 400,  100, 90,   50,  40,   10,  9,    5,   4,    1),
                               ('M',  'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')))

    def intToRoman(self, num: int) -> str:
        res = ''
        for i, r in self.digits.items():
            res += r * (num // i)
            num %= i
        return res


S = Solution()
intToRoman = S.intToRoman
print(intToRoman(3), 'III')
print(intToRoman(58), 'LVIII')
print(intToRoman(1994), 'MCMXCIV')
