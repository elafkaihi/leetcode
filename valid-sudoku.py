class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = {i:set() for i in range(9)}
        rows = {i:set() for i in range(9)}
        boxes = {(i,j):set() for i in range(3) for j in range(3)}
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue 
                elif board[r][c] in rows[r] or board[r][c] in columns[c] or board[r][c] in boxes[r//3,c//3]:
                    return False
                columns[c].add(board[r][c])
                rows[r].add(board[r][c])
                boxes[r//3,c//3].add(board[r][c])
        
        return True