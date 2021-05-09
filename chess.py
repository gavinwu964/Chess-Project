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

    def out_of_board(self):
        for i in self.targetSquare:
            if i < 0 or i > 7:
                self.isLegalMove = False

    def rock(self):
        """This method verifies whether a rock move is legal."""
        # Rock can only move horizontally or vertically.
        if self.currentSquare[0] != self.targetSquare[0] and \
                self.currentSquare[1] != self.targetSquare[1]:
            self.isLegalMove = False

        # Detects whether there are pieces blocking Rock's path.
        if self.currentSquare[0] == self.targetSquare[0]:  # Rock moves horizontally.
            for i in range(min(self.currentSquare[1], self.targetSquare[1]) + 1,
                           max(self.currentSquare[1], self.targetSquare[1])):
                if self.board[self.currentSquare[0]][i] != '00':
                    self.isLegalMove = False
                    break
        if self.currentSquare[1] == self.targetSquare[1]:  # Rock moves vertically.
            for i in range(min(self.currentSquare[0], self.targetSquare[0]) + 1,
                           max(self.currentSquare[0], self.targetSquare[0])):
                if self.board[i][self.currentSquare[0]] != '00':
                    self.isLegalMove = False
                    break

    def knight(self):
        """This method verifies whether a knight move is legal."""
