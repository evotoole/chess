from piece import Piece, Color
from typing import List
from illegalMoveError import IllegalMoveError

#TODO en passant and promotion

class Pawn(Piece):
    # def __init__(self, color: Color, current_pos: str): (inherited from Piece())

    def __repr__(self):
        return f'Pawn(colour= {self.color}, position= {self.current_pos})'

    # returns the non validated possible moves a piece can make
    def move(self, new_pos) -> List[str]:
        # returns two available moves if pawns are in starting position
        possible_moves = self.get_unvalidated_moves()
        for line in possible_moves:
            if new_pos in line:
                return line
            
        raise IllegalMoveError('new_pos is not a legal move for this piece (error in pawn.py)')
        

    def take(self) -> tuple [ List[str], List[str] ]:
        pass
       # return self.move_diagonally(1)

    def get_unvalidated_moves(self) -> List[List[str]]:
        x, y = ord(self.current_pos[0]), int(self.current_pos[1])
        possible_moves = [[]]

        LD = self.move_diagonally()[1]
        LU = self.move_diagonally()[0]
        RD = self.move_diagonally()[3]
        RU = self.move_diagonally()[2]
        
        if self.color == 'black':
            if y == 7:
                possible_moves.append(self.move_forward(2))
            else:
                possible_moves.append(self.move_forward(1))
            if len(LU) > 1:
                possible_moves.append([self.move_diagonally()[0][0]])
            if len(RU) > 1:
                possible_moves.append([self.move_diagonally()[2][0]])

        else: #white
            if y == 2:
                   possible_moves.append(self.move_backward(2))
            else:
                possible_moves.append(self.move_backward(1))
            if len(LU) > 1:
                possible_moves.append([self.move_diagonally()[1][0]])
            if len(RU) > 1:
                possible_moves.append([self.move_diagonally()[3][0]])
           
       
        
        return possible_moves


'''

p_white_start = Pawn(Color.white, 'd2')
p_white_moved = Pawn(Color.white, 'd3')


p_black_start = Pawn(Color.black, 'c6')
p_black_moved = Pawn(Color.black, 'd6')

print(p_black_start.get_unvalidated_moves())
#print(p_black_moved.get_unvalidated_moves())

'''

'''
print('Pawn Tests  move() START --------------')
print(f'white start {p_white_start.current_pos}: ', p_white_start.move())
print(f'white moved {p_white_moved.current_pos}: ', p_white_moved.move())

print(f'black start {p_black_start.current_pos}: ', p_black_start.move())
print(f'p_black_moved {p_black_moved.current_pos}: ', p_black_moved.move())
print('Pawn Tests move() END --------------\n')


p_take = Pawn(Color.white, 'd4')
print('Pawn Tests take() START --------------')
print(f'origin: [ {p_take.current_pos} ]: ', p_take.take())
print('Pawn Tests take() END --------------\n')

'''