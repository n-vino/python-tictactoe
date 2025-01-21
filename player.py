import math
import random

class Player:
    def __init__(self, letter):
        #letter is x or o for each player
        self.letter = letter
        
    def get_move(self, game):
        #get a player's next move
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        #user should be able to choose a valid empty spot
        valid_square = False
        value = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Enter move (0-8):')
            
            try:
                #check that this is a correct value by trying to cast into an integer
                value = int(square)
                #also check if the spot is not available
                if value not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
                
        return value
    
class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        #get a random empty spot for the computer's next spot
        square = random.choice(game.available_moves())
        return square