# https://leetcode.com/problems/3sum


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums_dict = {}
        for i, iv in enumerate(nums):
            nums_dict[iv] = i
            for j, jv in enumerate(nums[i + 1:]):
                diff = - iv - jv
                if diff in nums[i + j + 2:]:
                    for_add = sorted((iv, jv, diff))
                    if for_add not in res:
                        res.append(for_add)

        return res


S = Solution()
threeSum = S.threeSum
print(threeSum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]], sep='\n', end='\n\n')
print(threeSum([0, 1, 1]), [], sep='\n', end='\n\n')
print(threeSum([0, 0, 0]), [[0, 0, 0]], sep='\n', end='\n\n')
print(threeSum([1, 2, -2, -1]), [], sep='\n', end='\n\n')
