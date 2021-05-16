class Chess:
    """"""

    def __init__(self):
        self.board = [['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
                      ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
                      ['00', '00', '00', '00', '00', '00', '00', '00'],
                      ['00', '00', '00', '00', '00', '00', '00', '00'],
                      ['00', '00', '00', '00', '00', '00', '00', '00'],
                      ['00', '00', '00', '00', '00', '00', '00', '00'],
                      ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
                      ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']]
        self.pieceColor = {'White': ['wP', 'wR', 'wN', 'wB', 'wQ', 'wK'],
                           'Black': ['bP', 'bR', 'bN', 'bB', 'bQ', 'bK']}
        self.currentSquare = [-1, -1]
        self.targetSquare = [-1, -1]
        self.isLegalMove = True

    def compare_color(self, p1r, p1f, p2r, p2f):
        """This method takes coordinates of two pieces and compares colors between them."""
        if ((self.board[p1r][p1f] in self.pieceColor['White'] and
             self.board[p2r][p2f] in self.pieceColor['Black']) or
                (self.board[p1r][p1f] in self.pieceColor['Black'] and
                 self.board[p2r][p2f] in self.pieceColor['White'])):
            return 1
        else:
            return 0


class LegalSquares(Chess):
    """This class generates a list of piece's legal squares."""

    def __init__(self):
        super().__init__()
        self._pieceType = {'Pawn': ['wP', 'bP'], 'Rook': ['wR', 'bR'],
                           'Knight': ['wN', 'bN'], 'Bishop': ['wB', 'bB'],
                           'Queen': ['wQ', 'bQ'], 'King': ['wK', 'bK']}
        self.run(self.currentSquare[0], self.currentSquare[1], self.targetSquare)

    def rook(self, rank, file):
        """This method generates a list of Rook's legal squares."""
        result = []
        # Generates legal squares vertically.
        for i in range(1, rank + 1):  # going upwards
            if self.board[rank - i][file] != '00':
                if self.compare_color(rank, file, rank - i, file) == 1:
                    result.append([rank - i, file])
                break
            result.append([rank - i, file])
        for i in range(rank + 1, 8):  # going downwards
            if self.board[i][file] != '00':
                if self.compare_color(rank, file, i, file) == 1:
                    result.append([i, file])
                break
            result.append([i, file])

        # Generates legal squares horizontally.
        for i in range(1, file + 1):  # going to the left
            if self.board[rank][file - i] != '00':
                if self.compare_color(rank, file, rank, file - i) == 1:
                    result.append([rank, file - i])
                break
            result.append([rank, file - i])
        for i in range(file + 1, 8):  # going to the right
            if self.board[rank][i] != '00':
                if self.compare_color(rank, file, rank, i) == 1:
                    result.append([rank, i])
                break
            result.append([rank, i])
        return result

    def bishop(self, rank, file):
        """This method generates a list of Bishop's legal squares."""
        result = []
        # Generates legal squares for upper right.
        for i in range(1, min(rank + 1, 8 - file)):
            if self.board[rank - i][file + i] != '00':
                if self.compare_color(rank, file, rank - i, file + i) == 1:
                    result.append([rank - i, file + i])
                break
            result.append([rank - i, file + i])

        # Generate legal squares for upper left.
        for i in range(1, min(rank + 1, file + 1)):
            if self.board[rank - i][file - i] != '00':
                if self.compare_color(rank, file, rank - i, file - i) == 1:
                    result.append([rank - i, file - i])
                break
            result.append([rank - i, file - i])

        # Generate legal squares for lower left.
        for i in range(1, min(8 - rank, file + 1)):
            if self.board[rank + i][file - i] != '00':
                if self.compare_color(rank, file, rank + i, file - i) == 1:
                    result.append([rank + i, file - i])
                break
            result.append([rank + i, file - i])

        # Generate legal squares for lower right.
        for i in range(1, min(8 - rank, 8 - file)):
            if self.board[rank + i][file + i] != '00':
                if self.compare_color(rank, file, rank + i, file + i) == 1:
                    result.append([rank + i, file + i])
                break
            result.append([rank + i, file + i])
        return result

    def queen(self, rank, file):
        """This method generates a list of Queen's legal squares."""
        return self.rook(rank, file) + self.bishop(rank, file)

    def knight(self, rank, file):
        """This method generates a list of Knight's legal squares."""
        result = []
        potential_squares = [[rank + 1, file + 2], [rank + 1, file - 2], [rank - 1, file + 2],
                             [rank - 1, file - 2], [rank + 2, file + 1], [rank + 2, file - 1],
                             [rank - 2, file + 1], [rank - 2, file - 1]]
        for square in potential_squares:
            if 0 <= square[0] <= 7 and 0 <= square[1] <= 7:
                if self.board[square[0]][square[1]] == '00' or \
                        self.compare_color(rank, file, square[0], square[1]) == 1:
                    result.append(square)
        return result

    def pawn(self, rank, file):
        """This method generates a list of Pawn's legal squares."""
        result = []
        if self.board[rank][file] in self.pieceColor['White']:
            if self.board[rank - 1][file] == '00':
                result.append([rank - 1, file])
            if file != 0:
                if self.board[rank - 1][file - 1] in self.pieceColor['Black']:
                    result.append([rank - 1, file - 1])
            if file != 7:
                if self.board[rank - 1][file + 1] in self.pieceColor['Black']:
                    result.append([rank - 1, file + 1])
        else:
            if self.board[rank + 1][file] == '00':
                result.append([rank + 1, file])
            if file != 0:
                if self.board[rank + 1][file - 1] in self.pieceColor['White'] and file != 0:
                    result.append([rank + 1, file - 1])
            if file != 7:
                if self.board[rank + 1][file + 1] in self.pieceColor['White'] and file != 7:
                    result.append([rank + 1, file + 1])
        return result

    def brave_king(self, rank, file):
        """This method generates a list of King's legal squares without checking danger square."""
        result = []
        potential_squares = [[rank + 1, file - 1], [rank + 1, file], [rank + 1, file + 1],
                             [rank, file - 1], [rank, file + 1], [rank - 1, file - 1],
                             [rank - 1, file], [rank - 1, file + 1]]
        for square in potential_squares:
            if 0 <= square[0] <= 7 and 0 <= square[1] <= 7:
                if self.board[square[0]][square[1]] == '00' or \
                        self.compare_color(rank, file, square[0], square[1]) == 1:
                    result.append(square)
        return result

    def danger_squares(self, rank, file):
        """This method generates a list of King's danger squares."""
        result = []
        if self.board[rank][file] in self.pieceColor['White']:  # for White King
            for i in range(8):
                for j in range(8):
                    danger_squares = []
                    if self.board[i][j] == 'bP':
                        danger_squares.extend(self.pawn(i, j))
                    elif self.board[i][j] == 'bR':
                        danger_squares.extend(self.rook(i, j))
                    elif self.board[i][j] == 'bN':
                        danger_squares.extend(self.knight(i, j))
                    elif self.board[i][j] == 'bB':
                        danger_squares.extend(self.bishop(i, j))
                    elif self.board[i][j] == 'bQ':
                        danger_squares.extend(self.queen(i, j))
                    elif self.board[i][j] == 'bK':
                        danger_squares.extend(self.brave_king(i, j))
                    for square in danger_squares:  # prevent duplicates list in result
                        if square not in result:
                            result.extend(danger_squares)
        if self.board[rank][file] in self.pieceColor['Black']:  # for Black King
            for i in range(8):
                for j in range(8):
                    danger_squares = []
                    if self.board[i][j] == 'wP':
                        danger_squares.extend(self.pawn(i, j))
                    elif self.board[i][j] == 'wR':
                        danger_squares.extend(self.rook(i, j))
                    elif self.board[i][j] == 'wN':
                        danger_squares.extend(self.knight(i, j))
                    elif self.board[i][j] == 'wB':
                        danger_squares.extend(self.bishop(i, j))
                    elif self.board[i][j] == 'wQ':
                        danger_squares.extend(self.queen(i, j))
                    elif self.board[i][j] == 'wK':
                        danger_squares.extend(self.brave_king(i, j))
                    for square in danger_squares:  # prevent duplicates list in result
                        if square not in result:
                            result.extend(danger_squares)
        return result

    @staticmethod
    def king(potential_squares, danger_squares):
        """This method generates a list of King's legal squares."""
        result = []
        for square in potential_squares:
            if square not in danger_squares:
                result.append(square)
        return result

    def run(self, rank, file, target):
        """This method checks whether target is a legal square."""
        if self.board[rank][file] in self._pieceType['Pawn']:
            if target not in self.pawn(rank, file):
                self.isLegalMove = False
        elif self.board[rank][file] in self._pieceType['Rook']:
            if target not in self.rook(rank, file):
                self.isLegalMove = False
        elif self.board[rank][file] in self._pieceType['Knight']:
            if target not in self.knight(rank, file):
                self.isLegalMove = False
        elif self.board[rank][file] in self._pieceType['Bishop']:
            if target not in self.bishop(rank, file):
                self.isLegalMove = False
        elif self.board[rank][file] in self._pieceType['Queen']:
            if target not in self.queen(rank, file):
                self.isLegalMove = False
        elif self.board[rank][file] in self._pieceType['King']:
            if target not in self.king(self.brave_king(rank, file),
                                       self.danger_squares(rank, file)):
                self.isLegalMove = False
