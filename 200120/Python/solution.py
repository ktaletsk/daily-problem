class TicTacToe(object):
    def __init__(self, n):
        # Fill this in.
        self.size = n
        self.board = [None] * n * n
        self.game_over = False
        
    def __repr__(self):
        result = ''
        for i in range(self.size):
            result += '|'
            for j in range(self.size):
                el = self.board[i*self.size + j]
                if el == None:
                    result += ' '
                elif el == 1:
                    result += 'X'
                elif el == 2:
                    result += 'O'
                result += '|'
            result += '\n'
        return result
    
    def isOnDiagonal(self, row, col):
        return row==col or row+col==self.size-1
    
    def getDiagonals(self, row, col):
        """
        Return the arrays of diagonals to which element with current row and column belong to
        """
        result = []
        if row==col:
            result.append([self.board[i*self.size+i] for i in range(self.size)])
        if row+col==self.size-1:
            result.append([self.board[i*self.size+(self.size-1-i)] for i in range(self.size)])
        return result
    
    def getVertical(self, row):
        return [self.board[i*self.size+row] for i in range(self.size)]
    
    def getHorizontal(self, col):
        return [self.board[col*self.size+i] for i in range(self.size)]
        
    def check_win(self, row, col):
        """
        Checks if the newly added move won is the winning move
        """
        
        lines = []
        if self.isOnDiagonal(row,col):
            lines += self.getDiagonals(row,col)
        lines.append(self.getHorizontal(row))
        lines.append(self.getVertical(col))
        return any([len(set(line))==1 for line in lines])

    def move(self, row, col, player):
        # Fill this in.
        if row<self.size and row>=0 and col<self.size and col>=0 and player in (1,2) and not self.game_over:
            pos = row * self.size + col
            if self.board[pos] == None:
                self.board[pos] = player
            
                print(self)
                if self.check_win(row, col):
                    self.game_over = True
                    print('Player ' + ('X','O')[player-1] + ' wins!')
                return
        print('Move is not allowed')

def test_3():
    board = TicTacToe(3)
    print(board)
    board.move(0, 0, 1)
    board.move(0, 2, 2)
    board.move(2, 2, 1)
    board.move(2, 0, 1)
    board.move(1, 0, 2)
    board.move(2, 1, 1)
    assert board.check_win(2,1)

def test_5():
    board = TicTacToe(5)
    print(board)
    board.move(2, 2, 1)
    board.move(0, 2, 2)
    board.move(3, 3, 1)
    board.move(0, 3, 2)
    board.move(4, 4, 1)
    board.move(0, 1, 2)
    board.move(1, 1, 1)
    board.move(0, 4, 2)
    board.move(0, 0, 1)
    assert board.check_win(0,0)