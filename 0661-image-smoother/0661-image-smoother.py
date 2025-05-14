from typing import List

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img), len(img[0])
        result = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                total = 0
                count = 0
                # Check the 3x3 grid centered at (r, c)
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            total += img[nr][nc]
                            count += 1
                result[r][c] = total // count  # Integer division (floor)
        return result
