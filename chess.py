class GamePrep:
    """This class prepares the chess game."""

    def __init__(self):
        self.pieceColor = {'White': ['wP', 'wR', 'wN', 'wB', 'wQ', 'wK'],
                           'Black': ['bP', 'bR', 'bN', 'bB', 'bQ', 'bK']}
        self.pieceType = {'Pawn': ['wP', 'bP'], 'Rook': ['wR', 'bR'],
                          'Knight': ['wN', 'bN'], 'Bishop': ['wB', 'bB'],
                          'Queen': ['wQ', 'bQ'], 'King': ['wK', 'bK']}

    def compare_color(self, board, p1r, p1f, p2r, p2f):
        """This method takes coordinates of two pieces and compares colors between them."""
        if ((board[p1r][p1f] in self.pieceColor['White'] and
             board[p2r][p2f] in self.pieceColor['Black']) or
            (board[p1r][p1f] in self.pieceColor['Black'] and
             board[p2r][p2f] in self.pieceColor['White'])):
            return True

    def pawn(self, board, rank, file):
        """This method generates a list of Pawn's legal squares."""
        result = []
        if board[rank][file] in self.pieceColor['White']:
            if board[rank - 1][file] == '00':
                result.append([rank - 1, file])
            if file != 0:
                if board[rank - 1][file - 1] in self.pieceColor['Black']:
                    result.append([rank - 1, file - 1])
            if file != 7:
                if board[rank - 1][file + 1] in self.pieceColor['Black']:
                    result.append([rank - 1, file + 1])
        else:
            if board[rank + 1][file] == '00':
                result.append([rank + 1, file])
            if file != 0:
                if board[rank + 1][file - 1] in self.pieceColor['White']:
                    result.append([rank + 1, file - 1])
            if file != 7:
                if board[rank + 1][file + 1] in self.pieceColor['White']:
                    result.append([rank + 1, file + 1])
        return result

    def rook(self, board, rank, file):
        """This method generates a list of Rook's legal squares."""
        result = []
        # Generates legal squares vertically.
        for i in range(1, rank + 1):  # going upwards
            if board[rank - i][file] != '00':
                if self.compare_color(board, rank, file, rank - i, file):
                    result.append([rank - i, file])
                break
            result.append([rank - i, file])
        for i in range(rank + 1, 8):  # going downwards
            if board[i][file] != '00':
                if self.compare_color(board, rank, file, i, file):
                    result.append([i, file])
                break
            result.append([i, file])

        # Generates legal squares horizontally.
        for i in range(1, file + 1):  # going to the left
            if board[rank][file - i] != '00':
                if self.compare_color(board, rank, file, rank, file - i):
                    result.append([rank, file - i])
                break
            result.append([rank, file - i])
        for i in range(file + 1, 8):  # going to the right
            if board[rank][i] != '00':
                if self.compare_color(board, rank, file, rank, i):
                    result.append([rank, i])
                break
            result.append([rank, i])
        return result

    def knight(self, board, rank, file):
        """This method generates a list of Knight's legal squares."""
        result = []
        potential_squares = [[rank + 1, file + 2], [rank + 1, file - 2], [rank - 1, file + 2],
                             [rank - 1, file - 2], [rank + 2, file + 1], [rank + 2, file - 1],
                             [rank - 2, file + 1], [rank - 2, file - 1]]
        for square in potential_squares:
            if 0 <= square[0] <= 7 and 0 <= square[1] <= 7:
                if board[square[0]][square[1]] == '00' or \
                        self.compare_color(board, rank, file, square[0], square[1]):
                    result.append(square)
        return result

    def bishop(self, board, rank, file):
        """This method generates a list of Bishop's legal squares."""
        result = []
        # Generates legal squares for upper right.
        for i in range(1, min(rank + 1, 8 - file)):
            if board[rank - i][file + i] != '00':
                if self.compare_color(board, rank, file, rank - i, file + i):
                    result.append([rank - i, file + i])
                break
            result.append([rank - i, file + i])

        # Generate legal squares for upper left.
        for i in range(1, min(rank + 1, file + 1)):
            if board[rank - i][file - i] != '00':
                if self.compare_color(board, rank, file, rank - i, file - i):
                    result.append([rank - i, file - i])
                break
            result.append([rank - i, file - i])

        # Generate legal squares for lower left.
        for i in range(1, min(8 - rank, file + 1)):
            if board[rank + i][file - i] != '00':
                if self.compare_color(board, rank, file, rank + i, file - i):
                    result.append([rank + i, file - i])
                break
            result.append([rank + i, file - i])

        # Generate legal squares for lower right.
        for i in range(1, min(8 - rank, 8 - file)):
            if board[rank + i][file + i] != '00':
                if self.compare_color(board, rank, file, rank + i, file + i):
                    result.append([rank + i, file + i])
                break
            result.append([rank + i, file + i])
        return result

    def queen(self, board, rank, file):
        """This method generates a list of Queen's legal squares."""
        return self.rook(board, rank, file) + self.bishop(board, rank, file)

    def brave_king(self, board, rank, file):
        """This method generates a list of King's legal squares without checking danger square."""
        result = []
        potential_squares = [[rank + 1, file - 1], [rank + 1, file], [rank + 1, file + 1],
                             [rank, file - 1], [rank, file + 1], [rank - 1, file - 1],
                             [rank - 1, file], [rank - 1, file + 1]]
        for square in potential_squares:
            if 0 <= square[0] <= 7 and 0 <= square[1] <= 7:
                if board[square[0]][square[1]] == '00' or \
                        self.compare_color(board, rank, file, square[0], square[1]):
                    result.append(square)
        return result

    def danger_squares(self, board, rank, file):
        """This method generates a list of King's danger squares."""
        result = []
        temp = {}
        potential_king_squares = [[rank + 1, file - 1], [rank + 1, file], [rank + 1, file + 1],
                                  [rank, file - 1], [rank, file + 1], [rank - 1, file - 1],
                                  [rank - 1, file], [rank - 1, file + 1]]
        # Since moving a piece to a square occupied by a piece of the same color is
        # illegal, there are cases that opponent's piece around the king is guarded, but
        # the square occupied by this piece is not marked as a danger square. Turn every
        # opponent's pieces around the king into opposite-color pieces can resolve this problem.
        for square in potential_king_squares:
            if self.compare_color(board, rank, file, square[0], square[1]):
                temp[board[square[0]][square[1]]] = square
                if board[square[0]][square[1]] in self.pieceColor['White']:
                    board[square[0]][square[1]] = 'bP'
                else:
                    board[square[0]][square[1]] = 'wP'

        if board[rank][file] in self.pieceColor['White']:
            for i in range(8):
                for j in range(8):
                    danger_squares = []
                    if board[i][j] == 'bP':
                        if j != 0:
                            danger_squares.append([i + 1, j - 1])
                        if j != 7:
                            danger_squares.append([i + 1, j + 1])
                    elif board[i][j] == 'bR':
                        danger_squares.extend(self.rook(board, i, j))
                    elif board[i][j] == 'bN':
                        danger_squares.extend(self.knight(board, i, j))
                    elif board[i][j] == 'bB':
                        danger_squares.extend(self.bishop(board, i, j))
                    elif board[i][j] == 'bQ':
                        danger_squares.extend(self.queen(board, i, j))
                    elif board[i][j] == 'bK':
                        danger_squares.extend(self.brave_king(board, i, j))
                    for square in danger_squares:  # prevent duplicate lists in result
                        if square not in result:
                            result.append(square)
        else:
            for i in range(8):
                for j in range(8):
                    danger_squares = []
                    if board[i][j] == 'wP':
                        if j != 0:
                            danger_squares.append([i - 1, j - 1])
                        if j != 7:
                            danger_squares.append([i - 1, j + 1])
                    elif board[i][j] == 'wR':
                        danger_squares.extend(self.rook(board, i, j))
                    elif board[i][j] == 'wN':
                        danger_squares.extend(self.knight(board, i, j))
                    elif board[i][j] == 'wB':
                        danger_squares.extend(self.bishop(board, i, j))
                    elif board[i][j] == 'wQ':
                        danger_squares.extend(self.queen(board, i, j))
                    elif board[i][j] == 'wK':
                        danger_squares.extend(self.brave_king(board, i, j))
                    for square in danger_squares:  # prevent duplicate lists in result
                        if square not in result:
                            result.append(square)

        for piece, square in temp.items():  # revert the chess board
            board[square[0]][square[1]] = piece
        return result

    def king(self, board, rank, file):
        """This method generates a list of King's legal squares."""
        result = []
        for square in self.brave_king(board, rank, file):
            if square not in self.danger_squares(board, rank, file):
                result.append(square)
        return result

    def state(self, board, rank, file):
        """This method determines the game state."""
        game_state = {'isCheck': False, 'isStalemate': False, 'isCheckmate': False}
        if [rank, file] in self.danger_squares(board, rank, file):
            game_state['isCheck'] = True
        if not self.king(board, rank, file):
            game_state['isStalemate'] = True
        if game_state['isCheck'] is True and game_state['isStalemate'] is True:
            game_state['isCheckmate'] = True
            return game_state

    def legal(self, board, rank, file, target):
        """This method checks whether target is a legal square."""
        if board[rank][file] in self.pieceType['Pawn']:
            if target in self.pawn(board, rank, file):
                return True
        elif board[rank][file] in self.pieceType['Rook']:
            if target in self.rook(board, rank, file):
                return True
        elif board[rank][file] in self.pieceType['Knight']:
            if target in self.knight(board, rank, file):
                return True
        elif board[rank][file] in self.pieceType['Bishop']:
            if target in self.bishop(board, rank, file):
                return True
        elif board[rank][file] in self.pieceType['Queen']:
            if target in self.queen(board, rank, file):
                return True
        elif board[rank][file] in self.pieceType['King']:
            if target in self.king(board, rank, file):
                return True
