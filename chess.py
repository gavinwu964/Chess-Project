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
        self.currentSquare = [-1, -1]
        self.targetSquare = [-1, -1]
        self.isLegalMove = True


class LegalSquares(Chess):
    """This class generates a list of piece's legal squares."""

    def __init__(self):
        super().__init__()
        self._pieceTypes = {'Pawn': ['wP', 'bP'], 'Rook': ['wR', 'bR'],
                            'Knight': ['wN', 'bN'], 'Bishop': ['wB', 'bB'],
                            'Queen': ['wQ', 'bQ'], 'King': ['wK', 'bK']}
        self.run()

    def rook(self):
        """This method generates a list of Rook's legal squares."""
        result = []
        # Generates legal squares vertically.
        for i in range(1, self.currentSquare[0]):  # going upwards
            if self.board[i][self.currentSquare[1]] != '00':
                break
            result.append([i, self.currentSquare[1]])
        for i in range(self.currentSquare[0]+1, 8):  # going downwards
            if self.board[i][self.currentSquare[1]] != '00':
                break
            result.append([i, self.currentSquare[1]])

        # Generates legal squares Horizontally.
        for i in range(1, self.currentSquare[1]):  # going to the left
            if self.board[self.currentSquare[0]][i] != '00':
                break
            result.append([self.currentSquare[0], i])
        for i in range(self.currentSquare[1]+1, 8):  # going to the right
            if self.board[self.currentSquare[0]][i] != '00':
                break
            result.append([self.currentSquare[0], i])
        return result

    def run(self):
        """This method checks whether self.targetSquare is a legal square."""
        if self.board[self.currentSquare[0]][self.currentSquare[1]] in \
                self._pieceTypes['Pawn']:
            pass
        elif self.board[self.currentSquare[0]][self.currentSquare[1]] in \
                self._pieceTypes['Rook']:
            if self.targetSquare not in self.rook():
                self.isLegalMove = False
        elif self.board[self.currentSquare[0]][self.currentSquare[1]] in \
                self._pieceTypes['Knight']:
            pass
        elif self.board[self.currentSquare[0]][self.currentSquare[1]] in \
                self._pieceTypes['Bishop']:
            pass
        elif self.board[self.currentSquare[0]][self.currentSquare[1]] in \
                self._pieceTypes['Queen']:
            pass
        elif self.board[self.currentSquare[0]][self.currentSquare[1]] in \
                self._pieceTypes['King']:
            pass
