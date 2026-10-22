class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def valid_line(line):
            seen_cache = dict()
            for n in line: 
                if n == ".":
                    continue
                seen = seen_cache.get(n, False)
                if seen:
                    return False
                seen_cache[n] = True
            
            return True


        def valid_box(x, y):
            # convert a box to a line
            # y is row, x is col
            line = []
            for c in [x, x+1, x+2]: 
                for r in [y, y+1, y+2]:
                    cell = board[r][c]
                    line.append(cell)

            return valid_line(line)

        # check rows
        for row in board:
            if not valid_line(row):
                return False

        # check columns
        boardT = []
        for c in range(9):
            col = [row[c] for row in board]
            boardT.append(col)

        for row in boardT:
            if not valid_line(row):
                return False

        # check boxes
        # (0,0) ; (3,0) ; (6, 0)
        # (3,0)
        # (6,0)
        for x in [0, 3, 6]:
            for y in [0, 3, 6]:
                if not valid_box(x,y):
                    return False

        return True