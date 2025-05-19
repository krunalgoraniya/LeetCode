from typing import List

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = sorted(nums)

        # Check triangle inequality: sum of two smaller sides must be > third
        if a + b <= c:
            return "none"

        if a == b == c:
            return "equilateral"
        elif a == b or b == c or a == c:
            return "isosceles"
        else:
            return "scalene"
