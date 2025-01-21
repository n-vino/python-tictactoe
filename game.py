import time
from player import HumanPlayer, ComputerPlayer

class TicTacToe:
    def __init__(self):
        #list of length 9 to represent a 3x3 board
        self.board = [' '] * 9
        #to keep track of current winner
        self.current_winner = None
        
    def print_board(self):
        #slice board into 3 rows with 3 spots in each
        for row in [self.board[i*3 : (i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
            
    @staticmethod
    def print_board_nums():
        #static method bc doesn't relate to any specific board, no 'self'
        #to print out the number corresponding to each spots
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
            
    def available_moves(self):
        # moves = []
        # for (index, spot) in enumerate(self.board):
        #     #enumerate the spots on the board with an index
        #     #e.g. ['x', 'x', 'o'] -> [(0,'x'),(1, 'x'),(2,'o')]
        #     if spot == ' ':
        #         #if a spot is empty, append it to list of available moves
        #         moves.append(index)
        #     return moves
        
        return [i for i, x in enumerate(self.board) if x==' ']
        
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count()
    
    def make_move(self, square, letter):
        #if valid move, make move i.e. assign square to letter, return true
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.check_winner(square, letter):
                self.current_winner = letter
            return True
        #else if invalid move, return false
        return False
    
    def check_winner(self, square, letter):
        #declare winner if three in a row, column or diagonal
        #first check row 
        row_index = square // 3
        row = self.board[row_index * 3 : (row_index + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        #next check column
        col_index = square % 3
        column = [self.board[col_index + i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        #then check diagonals (all diagonal squares are even numbers)
        if square % 2 == 0:
            #check for first diagonal
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            #check for second diagonal
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
                return True
            
        #return false if all checks fail
        return False
        
def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()
        
    #starting letter
    letter = 'x'
        
    #iterate while the game still has empty squares
    while game.empty_squares():
        #get move from appropriate player
        if letter == 'o':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
            
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes move to square {square}')
                game.print_board()
                print('')
            
            #check if the player has won
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
            
            #other player's move now
            letter = 'o' if letter == 'x' else 'x'
            
        time.sleep(.8)
        
    if print_game:
        print('It\'s a tie!')
        
if __name__ == '__main__':
    x_player = HumanPlayer('x')
    o_player = ComputerPlayer('o')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)