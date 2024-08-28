class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: only one row
        if numRows == 1: return s

        rows = [[] for i in range(numRows)]

        currRow = 0
        maxRow = numRows - 1
        order = 1

        for ch in s:
            rows[currRow].append(ch)
            currRow += order
            if currRow == 0 or currRow == maxRow: order *= -1
        
        output = ""
        for r in rows:
            output += "".join(r)
        
        return output
        