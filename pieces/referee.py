from chessBoard import ChessBoard
from illegalMoveError import IllegalMoveError
from pawn import Pawn
from piece import Piece
from rook import Rook
from knight import Knight
from queen import Queen
from bishop import Bishop
from king import King
from typing import Any, List


class Referee:
    def __init__(self, white_check = False, black_check = False):
        self.chessboard_dict = ChessBoard().chessBoard
        self.white_check = white_check
        self.taken_by_white = []
        self.black_check = black_check
        self.taken_by_black = []


    def revert(self, prev_pos: str, curr_pos:str, taken_piece:object):
        self.chessboard_dict[prev_pos] = self.chessboard_dict[curr_pos]
        self.chessboard_dict[curr_pos] = taken_piece


    def checkmate(self)->bool:
        white_check = self.white_in_check('white')
        black_check = self.black_in_check('black')
        all_black_reached = self.get_all_reachable_black()
        #WORKS PROPERLY NOW
       
        all_white_reached = self.get_all_reachable_white()

        white_king_square = self.get_white_king_square()

        black_king_square = self.get_black_king_square()
       
      # RETURNS PROPER KING SQUARES FOR BOTH.
        white_king = self.chessboard_dict[white_king_square]
        black_king = self.chessboard_dict[black_king_square]
        #if we are currently in check


        if white_check:
            
            #get possible squares the white king can move to
            white_movable_squares = self.find_reachable_squares(white_king)
            for square in white_movable_squares:
                #if the king can move to a square that is not reachable by black it is not checkmate
                if square not in all_black_reached:
                    return False
            for piece in self.chessboard_dict.values():
                if piece.color == 'white':
                    if self.is_pinnable(piece):
                        return False
            return True
        
        if black_check:
     
            black_movable_squares = self.find_reachable_squares(black_king)
      
            for square in black_movable_squares:
                if square not in all_white_reached:
                    return False
  
            for piece in self.chessboard_dict.values():
                if piece == None:
                    pass
                elif piece.color == 'black':
                    if self.is_pinnable(piece):
                        return False
            return True
        
        return False


    def is_pinnable(self, piece: object)->bool:

        if piece.color == 'white':
            reachable = self.find_reachable_squares(piece)
            for square in reachable:
                move = self.move(piece.current_pos, square)
                if not self.white_in_check(piece.color):
                    self.revert(piece.current_pos, square, self.chessboard_dict[square])
                    return True
                elif move:
                    self.revert(piece.current_pos, square, self.chessboard_dict[square])
            return False
                 
        else:
            reachable = self.find_reachable_squares(piece)
            for square in reachable:
                move = self.move(piece.current_pos, square)
                if not self.black_in_check(piece.color):
                    self.revert(piece.current_pos, square, self.chessboard_dict[square])
                    return True
                elif move:
                    self.revert(piece.current_pos, square, self.chessboard_dict[square])
            return False
           
    
    def validate_move(self, curr_piece: object, new_pos:str, moves: List[str])->bool:
        current_pos = curr_piece.current_pos
        #checks if the square is in the possible moves for the piece
        #then checks if the move put ourselves in check (if it does we can't do the move)
        taken_piece = self.chessboard_dict[new_pos]

        if new_pos in moves:
            self.chessboard_dict[new_pos] = curr_piece
            self.chessboard_dict[current_pos] = None
            if curr_piece.color == 'white':
                self.white_check = self.white_in_check(curr_piece.color)
                if self.white_check:
                    self.revert(current_pos, new_pos, taken_piece)
                    return False
            else:
                self.black_check = self.black_in_check(curr_piece.color)
                if self.black_check:
                    self.revert(current_pos, new_pos, taken_piece)
                    return False
                

        self.revert(current_pos, new_pos, taken_piece)
        return True
        pass
    
    

    def white_in_check(self, color: str = 'white')->bool:
        white_king = self.get_white_king_square()
        black_reachable = self.get_all_reachable_black()
        if white_king in black_reachable:
            self.white_check = True
            return True
        self.white_check = False
        return False
    
        
    def black_in_check(self, color: str = 'black')->bool:
        black_king = self.get_black_king_square()
        white_reachable = self.get_all_reachable_white()
        if black_king in white_reachable:
            self.black_check = True
            return True
        self.black_check = False
        return False
    

    def get_white_king_square(self)->str:
        for object in self.chessboard_dict.values():
            if type(object) == King and object.color == 'white':
                return object.current_pos
        
    def get_black_king_square(self)->str:
        for object in self.chessboard_dict.values():
            if type(object) == King and object.color == 'black':
                return object.current_pos
            
    def get_all_reachable_white(self)->List[str]:
        reachable_squares = []
        for object in self.chessboard_dict.values():
            if object == None:
                continue
            elif object.color == 'white':
                
                reachable_squares.extend(self.find_reachable_squares(object))
        return reachable_squares
    
    def get_all_reachable_black(self)->List[str]:

        reachable_squares = []
        for object in self.chessboard_dict.values():
            if object == None:
                continue
            elif object.color == 'black':
                reachable_squares.extend(self.find_reachable_squares(object))


        return reachable_squares

    #when a piece takes another just replace one piece with the other, and change
    def take_square(self, piece: Piece, square: str):
        pass

    #returns all possible lines/paths for a given piece
    def find_reachable_squares(self, piece: Piece) -> List[str]:
        unvalidated_moves: List[List[str]] = piece.get_unvalidated_moves()
        ####I CURRENTLY LOOKING FOR e7!!!
     
        reachable_squares = []
      

        for line in unvalidated_moves:
            reachable_squares.extend(self.find_longest_sequence(line, piece))

       
        return reachable_squares
            
           
    def find_longest_sequence(self, line: List[str], piece: Piece) -> List[str]:
    
        reachable_line = []
        
        for square in line:
            if(self.chessboard_dict[square] == None):
                reachable_line.append(square)
            elif self.chessboard_dict[square].color != piece.color and type(piece) != Pawn:
                reachable_line.append(square)
                break
            elif self.chessboard_dict[square].color != piece.color:
                if piece.current_pos[0] != square[0]:
                    reachable_line.append(square)
                break
            else:
                break
       
        return reachable_line

    def move(self, curr_pos: str, new_pos: str) -> bool:
            curr_piece = self.chessboard_dict[ curr_pos ]
            taken_piece = self.chessboard_dict[ new_pos ]
            valid_moves = self.find_reachable_squares(curr_piece)

            valid_move = self.validate_move(curr_piece, new_pos, valid_moves)
            if not valid_move:
                return False

            # remove opponent piece and add it to list of taken pieces
            if isinstance(taken_piece, Piece): 
                if curr_piece.color == 'white':
                    self.taken_by_white.append(taken_piece)
                else:
                    self.taken_by_black.append(taken_piece)

            # update gameboard with moved piece
            self.chessboard_dict[ curr_piece.current_pos ] = None
            self.chessboard_dict[ new_pos ] = curr_piece 
            curr_piece.current_pos = new_pos

            self.black_in_check()
            self.white_in_check()
            mate = self.checkmate()
            if mate:
                if self.white_check:
                    raise IllegalMoveError('CHECKMATE: BLACK WINS')
                else:
                    raise IllegalMoveError('CHECKMATE: WHITE WINS')

            return True
    

'''


print('BEGIN TESTING REFEREE ------------REACHABLE SQUARES')
print('testing starting points in chessboard: only pawns and knights can move')
ref = Referee()
print('TESTING ALL WHITE in initial position')
for i in range(ord('a'), ord('h')+1):
    print(ref.chessboard_dict[f'{chr(i)}2'])
    print(ref.find_reachable_squares(ref.chessboard_dict[f'{chr(i)}2']))
    print(ref.chessboard_dict[f'{chr(i)}1'])
    print(ref.find_reachable_squares(ref.chessboard_dict[f'{chr(i)}1']))
print('TESTING ALL BLACK in initial position')
for i in range(ord('a'), ord('h')+1):
    print(ref.chessboard_dict[f'{chr(i)}7'])
    print(ref.find_reachable_squares(ref.chessboard_dict[f'{chr(i)}7']))
    print(ref.chessboard_dict[f'{chr(i)}8'])
    print(ref.find_reachable_squares(ref.chessboard_dict[f'{chr(i)}8']))
print('testing pawn edge case')
print(ref.find_reachable_squares(Pawn('white', 'a6')))

print('MOVING PAWN')
ref.move('a2', 'a4')
ref.move('a4', 'a5')
ref.move('a5', 'a6')
ref.move('a6', 'b7')
print(ref.taken_by_white)

'''