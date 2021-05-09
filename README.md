# Chess

1. legal moves (knight, bishop...) !!! We kinda have two options here. The first option is 'Legal Moves' which what I did in the most recent patch. I had a flag, 'isLegalMove'. Once it encounters an illegal move, the flag changes to False and we can prompt the player for another move. The second option is 'Legal Square'. We can provide all the legal squares for the player, and any other squares are prohibited.
2. is board in check
3. is board stalemate
4. is board checkmate
5. is move a capture
6. pawn promotion
