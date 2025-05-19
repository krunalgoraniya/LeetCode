from typing import List

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result = set()

        # Try all permutations of 3 digits
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i == j or j == k or i == k:
                        continue

                    d1, d2, d3 = digits[i], digits[j], digits[k]

                    # Number must not start with 0 and must be even
                    if d1 != 0 and d3 % 2 == 0:
                        number = d1 * 100 + d2 * 10 + d3
                        result.add(number)

        return sorted(result)
