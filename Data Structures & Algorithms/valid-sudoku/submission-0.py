class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for block_row in range(0, 9, 3):
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
        return True
        


















