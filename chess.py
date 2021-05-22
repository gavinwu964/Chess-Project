class GamePrep:
    """This class prepares chess games."""

    def __init__(self):
        self.initialBoard = [['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
                             ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
                             ['00', '00', '00', '00', '00', '00', '00', '00'],
                             ['00', '00', '00', '00', '00', '00', '00', '00'],
                             ['00', '00', '00', '00', '00', '00', '00', '00'],
                             ['00', '00', '00', '00', '00', '00', '00', '00'],
                             ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
                             ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']]
        self.pieceColor = {'white': ['wP', 'wR', 'wN', 'wB', 'wQ', 'wK'],
                           'black': ['bP', 'bR', 'bN', 'bB', 'bQ', 'bK']}
        self.pieceType = {'pawn': ['wP', 'bP'], 'rook': ['wR', 'bR'],
                          'knight': ['wN', 'bN'], 'bishop': ['wB', 'bB'],
                          'queen': ['wQ', 'bQ'], 'king': ['wK', 'bK']}

    def color(self, board, piece1, piece2):
        """This method  compares color between two pieces."""
        if ((board[piece1[0]][piece1[1]] in self.pieceColor['white'] and
             board[piece2[0]][piece2[1]] in self.pieceColor['black']) or
            (board[piece1[0]][piece1[1]] in self.pieceColor['black'] and
             board[piece2[0]][piece2[1]] in self.pieceColor['white'])):
            return True

    def coordinate(self, board, piece, color):
        """This method returns the coordinates of specific piece(s)."""
        squares = []
        piece = set(self.pieceType[piece]).intersection(self.pieceColor[color]).pop()
        for rank in range(8):
            for file in range(8):
                if board[rank][file] == piece:
                    squares.append([rank, file])
        return squares

    def pawn(self, board, rank, file):
        """This method generates a list of Pawn's legal squares."""
        squares = []
        if board[rank][file] in self.pieceColor['white']:
            if board[rank - 1][file] == '00':
                squares.append([rank - 1, file])
            if file != 0:
                if board[rank - 1][file - 1] in self.pieceColor['black']:
                    squares.append([rank - 1, file - 1])
            if file != 7:
                if board[rank - 1][file + 1] in self.pieceColor['black']:
                    squares.append([rank - 1, file + 1])
        else:
            if board[rank + 1][file] == '00':
                squares.append([rank + 1, file])
            if file != 0:
                if board[rank + 1][file - 1] in self.pieceColor['white']:
                    squares.append([rank + 1, file - 1])
            if file != 7:
                if board[rank + 1][file + 1] in self.pieceColor['white']:
                    squares.append([rank + 1, file + 1])
        return squares

    def rook(self, board, rank, file):
        """This method generates a list of Rook's legal squares."""
        squares = []
        # Generates legal squares vertically.
        for i in range(1, rank + 1):  # going upwards
            if board[rank - i][file] != '00':
                if self.color(board, [rank, file], [rank - i, file]):
                    squares.append([rank - i, file])
                break
            squares.append([rank - i, file])
        for i in range(rank + 1, 8):  # going downwards
            if board[i][file] != '00':
                if self.color(board, [rank, file], [i, file]):
                    squares.append([i, file])
                break
            squares.append([i, file])

        # Generates legal squares horizontally.
        for i in range(1, file + 1):  # going to the left
            if board[rank][file - i] != '00':
                if self.color(board, [rank, file], [rank, file - i]):
                    squares.append([rank, file - i])
                break
            squares.append([rank, file - i])
        for i in range(file + 1, 8):  # going to the right
            if board[rank][i] != '00':
                if self.color(board, [rank, file], [rank, i]):
                    squares.append([rank, i])
                break
            squares.append([rank, i])
        return squares

    def knight(self, board, rank, file):
        """This method generates a list of Knight's legal squares."""
        squares = []
        potential_squares = [[rank + 1, file + 2], [rank + 1, file - 2], [rank - 1, file + 2],
                             [rank - 1, file - 2], [rank + 2, file + 1], [rank + 2, file - 1],
                             [rank - 2, file + 1], [rank - 2, file - 1]]
        for square in potential_squares:
            if 0 <= square[0] <= 7 and 0 <= square[1] <= 7:
                if board[square[0]][square[1]] == '00' or \
                        self.color(board, [rank, file], square):
                    squares.append(square)
        return squares

    def bishop(self, board, rank, file):
        """This method generates a list of Bishop's legal squares."""
        squares = []
        # Generates legal squares for upper right.
        for i in range(1, min(rank + 1, 8 - file)):
            if board[rank - i][file + i] != '00':
                if self.color(board, [rank, file], [rank - i, file + i]):
                    squares.append([rank - i, file + i])
                break
            squares.append([rank - i, file + i])

        # Generate legal squares for upper left.
        for i in range(1, min(rank + 1, file + 1)):
            if board[rank - i][file - i] != '00':
                if self.color(board, [rank, file], [rank - i, file - i]):
                    squares.append([rank - i, file - i])
                break
            squares.append([rank - i, file - i])

        # Generate legal squares for lower left.
        for i in range(1, min(8 - rank, file + 1)):
            if board[rank + i][file - i] != '00':
                if self.color(board, [rank, file], [rank + i, file - i]):
                    squares.append([rank + i, file - i])
                break
            squares.append([rank + i, file - i])

        # Generate legal squares for lower right.
        for i in range(1, min(8 - rank, 8 - file)):
            if board[rank + i][file + i] != '00':
                if self.color(board, [rank, file], [rank + i, file + i]):
                    squares.append([rank + i, file + i])
                break
            squares.append([rank + i, file + i])
        return squares

    def queen(self, board, rank, file):
        """This method generates a list of Queen's legal squares."""
        return self.rook(board, rank, file) + self.bishop(board, rank, file)

    def brave_king(self, board, rank, file):
        """This method generates a list of King's legal squares without checking danger square."""
        squares = []
        potential_squares = [[rank + 1, file - 1], [rank + 1, file], [rank + 1, file + 1],
                             [rank, file - 1], [rank, file + 1], [rank - 1, file - 1],
                             [rank - 1, file], [rank - 1, file + 1]]
        for square in potential_squares:
            if 0 <= square[0] <= 7 and 0 <= square[1] <= 7:
                if board[square[0]][square[1]] == '00' or \
                        self.color(board, [rank, file], square):
                    squares.append(square)
        return squares

    def danger_squares(self, board, rank, file):
        """This method generates a list of King's danger squares."""
        squares = []
        temp = {}
        potential_king_squares = [[rank + 1, file - 1], [rank + 1, file], [rank + 1, file + 1],
                                  [rank, file - 1], [rank, file + 1], [rank - 1, file - 1],
                                  [rank - 1, file], [rank - 1, file + 1]]
        # Since moving a piece to a square occupied by a piece of the same color is
        # illegal, there are cases that opponent's piece around the king is guarded, but
        # the square occupied by this piece is not marked as a danger square. Turn every
        # opponent's pieces around the king into opposite-color pieces can resolve this problem.
        for square in potential_king_squares:
            if self.color(board, [rank, file], square):
                temp[board[square[0]][square[1]]] = square
                if board[square[0]][square[1]] in self.pieceColor['white']:
                    board[square[0]][square[1]] = 'bP'
                else:
                    board[square[0]][square[1]] = 'wP'

        color = 'black' if board[rank][file] in self.pieceColor['white'] else 'white'
        for piece in self.pieceColor[color]:
            danger_square = []
            if piece == 'wP' or piece == 'bP':
                for square in self.coordinate(board, 'pawn', color):
                    danger_square.extend(self.pawn(board, square[0], square[1]))
            elif piece == 'wK' or piece == 'bK':
                for square in self.coordinate(board, 'king', color):
                    danger_square.extend(self.brave_king(board, square[0], square[1]))
            else:
                for piece_type in self.pieceType:
                    if piece in self.pieceType[piece_type]:
                        piece = piece_type
                for square in self.coordinate(board, piece, color):
                    danger_square.extend(getattr(GamePrep, piece)(self, board, square[0], square[1]))
            for square in danger_square:  # prevent duplicates
                if square not in squares:
                    squares.append(square)

        for piece, square in temp.items():  # revert the chess board
            board[square[0]][square[1]] = piece
        return squares

    def king(self, board, rank, file):
        """This method generates a list of King's legal squares."""
        squares = []
        for square in self.brave_king(board, rank, file):
            if square not in self.danger_squares(board, rank, file):
                squares.append(square)
        return squares

    def legal(self, board, rank, file, target):
        """This method checks whether target is a legal square."""
        for piece in self.pieceType:
            if board[rank][file] in self.pieceType[piece]:
                if target in getattr(GamePrep, piece)(self, board, rank, file):
                    return True

    def state(self, board, color):
        """This method determines the game state."""
        rank, file = self.coordinate(board, 'king', color)[0]
        game_state = {'isCheck': False, 'isStalemate': False, 'isCheckmate': False}
        if [rank, file] in self.danger_squares(board, rank, file):
            game_state['isCheck'] = True
        if not self.king(board, rank, file):
            game_state['isStalemate'] = True
        if game_state['isCheck'] is True and game_state['isStalemate'] is True:
            game_state['isCheckmate'] = True
        return game_state
