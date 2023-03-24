# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_dict = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in nums_dict:
                return [nums_dict[diff], i]
            nums_dict[v] = i


S = Solution()
twoSum = S.twoSum
print(twoSum([2, 7, 11, 15], 9), [0, 1])
print(twoSum([3, 2, 4], 6), [1, 2])
print(twoSum([3, 3], 6), [0, 1])
