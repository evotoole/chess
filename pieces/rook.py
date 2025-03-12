from piece import Piece, Color
from typing import List
from illegalMoveError import IllegalMoveError

class Rook(Piece):
    # Piece is initialized through colour and current position,(__init__ method in Piece class)
    def __str__(self):
        return f'ROOK:{self.current_pos}'
    
    def __repr__(self):
        return f'Rook(colour= {self.color}, position= {self.current_pos})'

    # returns the non validated possible moves a piece can make
    def move(self, new_pos: str) -> List[str]:
        x, y = self.current_pos[0], self.current_pos[1]
        x_index = self.cols.index(x)
        y_index = self.rows.index(y)

        #remove the current position from the possible moves
        possible_x = self.cols.copy()
        possible_x.pop(x_index)
        possible_y = self.rows.copy()
        possible_y.pop(y_index)

        #create our possible_moves array (these are the squares we can move to 
        #if there are no pieces in the way)
        possible_moves = []
        for i in possible_x: possible_moves.append(f'{i}{y}')
        for j in possible_y: possible_moves.append(f'{x}{j}')

        
        # triple nested if statements lol
        #TODO get referee to validate the move
        if new_pos in possible_moves:
            
            change_in_column = ord(self.current_pos[0]) - ord(new_pos[0])
            change_in_row =  int(self.current_pos[1]) - int(new_pos[1])

            if change_in_column != 0:
                if ((change_in_column > 0) and self.color == 'white')or\
                    ((change_in_column < 0) and self.color == 'black'):
                    return self.move_right(abs(change_in_column))
                else:
                    return self.move_left(abs(change_in_column))
        
                
            elif change_in_row != 0:
                
                if ((change_in_row > 0) and self.color == 'white')or\
                    ((change_in_row < 0) and self.color == 'black'):
                    
                    return self.move_backward(abs(change_in_row))
                else:
                    return self.move_backward(abs(change_in_row))
               
               
            else:
                raise IllegalMoveError("position has not changed (invalid new_pos value in rook.py)")
            
            
        raise IllegalMoveError('invalid move; piece cannot move in this way (invalid new_pos value in rook.py)')

        
    
    def take(self):
        return
    
    #this function returns the possible unvalidate moves a piece can make
    #these moves are grouped into paths/lines that we can take.
    def get_unvalidated_moves(self) -> List[List[str]]:
        x, y = self.current_pos[0], self.current_pos[1]
        x_index = self.cols.index(x)
        y_index = self.rows.index(y)

        #remove the current position from the possible moves
      
        #create our possible_moves array (these are the squares we can move to 
        #if there are no pieces in the way)
       
        
        b = self.move_forward(8)
        c = self.move_backward(8)
        d = self.move_right(8)
        e = self.move_left(8)
        a = self.move_diagonally()
       
        complete_arr = [b, c, d, e]
        complete_arr.extend(a)
        
        return complete_arr



'''
rook = Rook('white', 'a1')
#print('START ROOK TESTING--------')
print(rook.move('a5'))
try:
    rook.move('a1')
    print("FAIL!!!")
except IllegalMoveError as e:
    print('IllegalMoveError properly caught')

rook = Rook('black', 'h1')
print(rook.move('d1'))

try:
    rook.move('k1')
except IllegalMoveError as e:
    print('IllegalMoveError properly caught')

try:
    rook.move('b2')
except IllegalMoveError as e:
    print('IllegalMoveError properly caught')

'''