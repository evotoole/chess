from piece import Piece, Color
from typing import List
from illegalMoveError import IllegalMoveError

class Knight(Piece):
    # Piece is initialized through colour and current position,(__init__ method in Piece class)

    def __repr__(self):
        return f'Knight(colour= {self.color}, position= {self.current_pos})'

    def __str__(self):
        return f'KNIGHT:{self.current_pos}'
    # returns the non validated possible moves a piece can make
    def move(self, new_pos: str) -> List[str]:
      

        x, y = self.current_pos[0], self.current_pos[1]
        x_index = self.cols.index(x)
        y_index = self.rows.index(y)

        #get a list of all possible squares
        possible_moves = []
        possible_squares = []
        for i in range(len(self.cols)):
            for j in range(len(self.rows)):
                possible_squares.append(f'{self.cols[i]}{self.rows[j]}')

        #the following adds all moves which we can move 3 one direction and then 1 left or right. (legal knight moves)
        possible_moves = self.calculate_possible(possible_squares, x, y)

        #if the new position is in the set of possible moves then return that as a path
        #the knight jumps squares so the path to the new postion only contains the new position
        path = []
        if new_pos in possible_moves:
            path.append(self.current_pos)
            path.append(new_pos)
            return path
        
        #if its not a legal move (not in the possible moves) then throw an error
        raise IllegalMoveError('new_pos is not a legal move for this piece (error in knight.py)')
    
    def take():
        pass

    #this function checks which out of every square is currently reachable by the knight
    #this is done by subtracting from each square the amount a knight can move, to see
    #if the knight is reachable
    def calculate_possible(self, possible_squares, x, y) -> List[str]:
        possible_moves = []

        for square in possible_squares:
            if ((((chr(ord(square[0]) - 2) == x) or chr(ord(square[0]) + 2) == x))\
                and (((int(square[1]) - 1) == int(y)) or (int(square[1]) + 1 == int(y)))):

                possible_moves.append(square)
            
            elif (((int(square[1]) - 2 == int(y))) or (int(square[1]) + 2 == int(y)))\
                 and ((chr(ord(square[0]) - 1) == x) or (chr(ord(square[0]) + 1) == x)):
                
                possible_moves.append(square)

        return possible_moves

    def get_unvalidated_moves(self) -> List[List[str]]:
        x, y = self.current_pos[0], self.current_pos[1]
        x_index = self.cols.index(x)
        y_index = self.rows.index(y)

        #get a list of all possible squares
        possible_moves = []
        possible_squares = []
        for i in range(len(self.cols)):
            for j in range(len(self.rows)):
                possible_squares.append(f'{self.cols[i]}{self.rows[j]}')

        path_list = []
        #the following adds all moves which we can move 3 one direction and then 1 left or right. (legal knight moves)
        possible_moves = self.calculate_possible(possible_squares, x, y)
        for move in possible_moves:
            path_list.append([move])
        return path_list




