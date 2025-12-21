"""
twoSum
Created: 2025-12-21

Python 3.12.3
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = dict()  # {value: [indices]}
        for i in range(len(nums)):
            d[nums[i]] = d.get(nums[i], []) + [i]

        for i in nums:
            other_half = target - i
            if i == other_half:
                if len(d.get(i, [])) > 1:
                    indices = d.get(i)[:2]
                    return [indices[0], indices[1]]
            elif d.get(other_half, -10) != -10:
                return [d[i][0], d[other_half][0]]
        return []
