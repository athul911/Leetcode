class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or len(s) < 1:
            return s
        rows = [''] * numRows
        current = 0
        going_d = False

        for char in s:
            rows[current]+=char

            if current ==0 or current == numRows-1:
                going_d = not going_d
            
            current = current+1 if going_d else current-1

        return "".join(rows)