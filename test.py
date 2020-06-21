def main():
    def check(self, x, y):
        piece = self.board[x][y]

        # positive x direction
        pieces = list()
        for i in range(x + 1, 8):
            c_piece = self.board[i][y]
            if str(c_piece) == '0':
                break
            else:
                pieces.append(((i, y)))
        
        pieces.pop(-1)
        for piece in pieces:
            x,y = piece
            self.board[x][y].flip()
            # piece = [C, (x, y)], where C is the color of the piece.
            
        return pieces

if __name__ == '__main__':
    main()
