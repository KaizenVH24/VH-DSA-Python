class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        # rows = [""]*numRows
        # curr_row = 0
        # direction = 1 # up=-1, down=1

        # for ch in s:
        #     rows[curr_row] += ch

        #     if curr_row == 0:
        #         dirction = 1
        #     elif curr_row == numRows-1:
        #         direction = -1
            
        #     curr_row += direction
        # return ("".join(rows))

        res = []
        cycle = 2 * (numRows - 1)
        
        for row in range(numRows):
            for i in range(row, len(s), cycle):
                res.append(s[i])
                
                diag = i + cycle - 2 * row
                if row != 0 and row != numRows - 1 and diag < len(s):
                    res.append(s[diag])
        
        return "".join(res)