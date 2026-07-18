class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row_set = set()
            col_set = set()
            for j in range(9):
                # Check Row i
                row_val = board[i][j]
                if row_val != ".":
                    if row_val in row_set:
                        return False
                    row_set.add(row_val)
                
                # Check Column i
                col_val = board[j][i]
                if col_val != ".":
                    if col_val in col_set:
                        return False
                    col_set.add(col_val)

        # 2. VALIDATE 3x3 BLOCKS (Your logic, fixed)
        for block_row in range(0, 9, 3):
            for block_col in range(0, 9, 3):
                block_map = {}

                for r in range(block_row, block_row + 3):
                    for c in range(block_col, block_col + 3):
                        val = board[r][c]

                        if val != ".":
                            if val not in block_map:
                                block_map[val] = []
                            # FIX 1: Append must happen OUTSIDE the 'if not in' check
                            block_map[val].append((r, c))
                
                for k, i in block_map.items():
                    if len(i) > 1:
                        return False
                    
                # FIX 2: Removed 'else: return True' so the loop continues checking everything

        # If everything passes all checks, the board is valid
        return True
'''        for block_row in range(0, 9, 3):
            for block_col in range(0, 9, 3):
                block_map = {}

                for r in range(block_row, block_row + 3):
                    for c in range(block_col, block_col + 3):
                        val = board[r][c]

                        if val != ".":
                            if val not in block_map:
                                block_map[val] = []
                            block_map[val].append((r, c))
                
                for k, i in block_map.items():
                    if len(i) > 1:
                        return False
        return True'''
        


















