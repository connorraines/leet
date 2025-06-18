def convert(self, s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1 or numRows >= len(s):
        return s

    # Create an array of strings for each row
    rows = [''] * numRows
    current_row = 0
    going_down = False
    # Iterate through the characters in the string
    for char in s:
        # Place the character in the current row
        rows[current_row] += char
        if current_row == 0:
            going_down = True
        elif current_row == numRows - 1:
            going_down = False
        current_row += 1 if going_down else -1
    # Concatenate all rows to get the final result
    return ''.join(rows)
# Test case
s = "PAYPALISHIRING"
numRows = 3
solution = convert(None, s, numRows)
print(solution)  # Output: "PAHNAPLSIIGYIR"