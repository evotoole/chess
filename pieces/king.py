from piece import Piece, Color
from typing import List
from illegalMoveError import IllegalMoveError


class King(Piece):
    # Piece is initialized through colour and current position,(__init__ method in Piece class)
    
    def __init__(self, color: Color, current_pos: str, check = False):
        super().__init__(color, current_pos)
        self.check = check

    def take(self):
            pass
    
    def __str__(self):
        return f'KING:{self.current_pos}'
    
    def __repr__(self):
        return f'King(colour= {self.color}, position= {self.current_pos})'

    # returns the non validated possible moves a piece can make
    def move(self, new_pos: str) -> List[str]:
        possible_squares = self.get_unvalidated_moves()
        path = []
        for i in range(len(possible_squares)):
            if new_pos in possible_squares[i]:
                path.append(self.current_pos)
                path.append(new_pos)
                return path
        raise IllegalMoveError('new_pos is not a legal move for this piece (error in king.py)')


    def get_unvalidated_moves(self) -> List[List[str]]:
        x, y = self.current_pos[0], self.current_pos[1]
        x_index = self.cols.index(x)
        y_index = self.rows.index(y)

        #remove the current position from the possible moves
        right_index = x_index + 1
        left_index = x_index - 1

        possible_moves = []
        #create our possible_moves array (these are the squares we can move to 
        #if there are no pieces in the way)

        #check if our king is in the corner
        if (x == 'a' and y == '1') or (x == 'a' and y == '8') or (x == 'h' and y == '1') or (x == 'h' and y == '8'):
            if x == 'a':
                possible_moves.append([f'b{y}'])
            elif x == 'h':
                possible_moves.append([f'g{y}'])
            if y == '1':
                possible_moves.append([f'{x}2'])
            elif y == '8':
                possible_moves.append([f'{x}7'])
            if x == 'a' and y == '1':
                possible_moves.append([f'b2'])
            elif x == 'a' and y == '8':
                possible_moves.append([f'b7'])
            elif x == 'h' and y == '1':
                possible_moves.append([f'g2'])
            elif x == 'h' and y == '8':
                possible_moves.append([f'g7'])
            return possible_moves
        
        #otherwise check if our king is on the edge
        if (x == 'a') or (x == 'h') or (y == '1') or (y == '8'):
            if x == 'a':
                possible_moves.append([f'b{y}'])
            elif x == 'h':
                possible_moves.append([f'g{y}'])
            if y == '1':
                possible_moves.append([f'{x}2'])
            elif y == '8':
                possible_moves.append([f'{x}7'])
            return possible_moves
        

        #otherwise king has all possible moves around it
        possible_moves = [[f'{x}{self.rows[y_index+1]}'],
                        [f'{self.cols[x_index-1]}{self.rows[y_index+1]}'],
                        [f'{self.cols[x_index+1]}{self.rows[y_index+1]}'],
                        [f'{self.cols[x_index-1]}{y}'],
                        [f'{self.cols[x_index+1]}{y}'],
                        [f'{self.cols[x_index+1]}{self.rows[y_index-1]}'],
                        [f'{self.cols[x_index-1]}{self.rows[y_index-1]}'],
                        [f'{x}{self.rows[y_index-1]}']]
        
        return possible_moves

        

