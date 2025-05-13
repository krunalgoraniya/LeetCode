class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create a list of empty strings for each row
        rows = [''] * numRows
        current_row = 0
        going_down = False
        
        # Iterate through the characters in the string
        for char in s:
            # Add the character to the current row
            rows[current_row] += char
            
            # If we're at the first or last row, change direction
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            
            # Move up or down the rows
            current_row += 1 if going_down else -1
        
        # Join all rows to form the final zigzag pattern
        return ''.join(rows)
 