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
        self.isCheck = False
        self.isCheckmate = False
        self.isStalemate = False
        self.isLegalMove = True


class LegalMove(Chess):
    """"""

    def __init__(self):
        super().__init__()
        self._whitePieces = ['wP', 'wR', 'wN', 'wB', 'wQ', 'wK']
        self._blackPieces = ['bP', 'bR', 'bN', 'bB', 'bQ', 'bK']
        self._rook = ['wR', 'bR']
        self.main()

    def out_of_board(self):
        for i in self.targetSquare:
            if i < 0 or i > 7:
                self.isLegalMove = False

    def self_capture(self):
        if self.board[self.currentSquare[0]][self.currentSquare[1]] in self._whitePieces:
            if self.board[self.targetSquare[0]][self.targetSquare[1]] in self._whitePieces:
                self.isLegalMove = False
        if self.board[self.currentSquare[0]][self.currentSquare[1]] in self._blackPieces:
            if self.board[self.targetSquare[0]][self.targetSquare[1]] in self._blackPieces:
                self.isLegalMove = False

    def rook(self):
        """This method verifies whether a rook move is legal."""
        # Rook can only move horizontally or vertically.
        if self.currentSquare[0] != self.targetSquare[0] and \
                self.currentSquare[1] != self.targetSquare[1]:
            self.isLegalMove = False

        # Detects whether there are pieces blocking Rook's path.
        if self.currentSquare[0] == self.targetSquare[0]:  # Rook moves horizontally.
            for i in range(min(self.currentSquare[1], self.targetSquare[1]) + 1,
                           max(self.currentSquare[1], self.targetSquare[1])):
                if self.board[self.currentSquare[0]][i] != '00':
                    self.isLegalMove = False
                    break
        if self.currentSquare[1] == self.targetSquare[1]:  # Rook moves vertically.
            for i in range(min(self.currentSquare[0], self.targetSquare[0]) + 1,
                           max(self.currentSquare[0], self.targetSquare[0])):
                if self.board[i][self.currentSquare[0]] != '00':
                    self.isLegalMove = False
                    break

    def knight(self):
        """This method verifies whether a knight move is legal."""

    def main(self):
        self.out_of_board()
        self.self_capture()
        # Rook:
        if self.board[self.currentSquare[0]][self.currentSquare[1]] in self._rook:
            self.rook()
