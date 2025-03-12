from pawn import Pawn
from queen import Queen
from knight import Knight
from rook import Rook
from bishop import Bishop
from king import King



class ChessBoard:


    def __init__(self, as_white = True):
        
            #The chess board is read as each sub array being a row on the chess board.
            #The start of the array is the side facing the user.
            #maybe change each of these numbers into piece classes
            #EVAN: Rook, Knight, Queen
            #Raul: Bishop, King, Pawn
            #
   
        self.pieceLocations = [
            [Rook("white", 'a1'), Knight("white", 'b1'), Bishop("white", 'c1'), Queen("white", 'd1'), King("white", 'e1'), Bishop("white", 'f1'), Knight("white", 'g1'), Rook("white", 'h1')],
            [Pawn("white", 'a2'), Pawn("white", 'b2'), Pawn("white", 'c2'), Pawn("white", 'd2'), Pawn("white", 'e2'), Pawn("white", 'f2'), Pawn("white", 'g2'), Pawn("white", 'h2')],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [Pawn("black", 'a7'), Pawn("black", 'b7'), Pawn("black", 'c7'), Pawn("black", 'd7'), Pawn("black", 'e7'), Pawn("black", 'f7'), Pawn("black", 'g7'), Pawn("black", 'h7')],
            [Rook("black", 'a8'), Knight("black", 'b8'), Bishop("black", 'c8'), Queen("black", 'd8'), King("black", 'e8'), Bishop("black", 'f8'), Knight("black", 'g8'), Rook("black", 'h8')]
        ]

        #we will represent the chessboard as a dictionary with each sqaure given
        #its proper letter and number as a key. its value will be the piece at that
        #square

        self.chessBoard = {}

        #the ASCII value for 'a' in python is 97. so subtract 97 to access index 0.

        for column in range(ord('a'), ord('h')+1):
            for row in range(1, 9):
                try:
                    self.pieceLocations[row-1][column-97].current_pos = f"{chr(column)}{row}"
                    self.chessBoard[f"{chr(column)}{row}"] = self.pieceLocations[row-1][column-97]
                except:
                    self.chessBoard[f"{chr(column)}{row}"] = None


     
    #def move(piece, prev_pos_row,prev_pos_column, new_pos_row, new_pos_column):
        #make a .get_type for each piece
        #self.chessBoard[]
'''
chessboard = ChessBoard()
print(chessboard.chessBoard)
'''