class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #create 3 hashsets to determine whether the grid is valid or not
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        #iterate through entire grid
        for r in range(9):
            for c in range(9):

                #if the space is empty, continue
                if board[r][c] == ".":
                    continue
                
                #if value already seen in current row or column or current 3x3 square, then return false
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or squares[r//3, c//3]):
                    return False

                #adds the value to the hashsets to make sure that they are updated
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[r//3, c//3].add(board[r][c])
        
        return True
