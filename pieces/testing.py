import unittest
from chessBoard import ChessBoard
from pawn import Pawn
from rook import Rook
from knight import Knight
from queen import Queen
from bishop import Bishop
from king import King
from typing import List
from piece import Color
from referee import Referee
from illegalMoveError import IllegalMoveError

'''
print("TESTING MOVE METHODS____________________________________________")
r1 = Referee()
r1.move('e2', 'e4')
print(r1.chessboard_dict['e2'])
print(r1.chessboard_dict['e4'])
r1.move('d2', 'd4')
print(r1.chessboard_dict['d2'])
print(r1.chessboard_dict['d4'])
r1.move('c1', 'f4')
print(r1.chessboard_dict['c1'])
print(r1.chessboard_dict['f4'])
print(r1.chessboard_dict['f4'].get_unvalidated_moves())

'''



class TestGame(unittest.TestCase):
    def test_games(self):
        #Testing a basic game that ends quickly (scholars mate)
        r1 = Referee()
        r1.move('e2', 'e4')
        r1.move('e7', 'e5')
        r1.move('f1', 'c4')
        r1.move('b8', 'c6')
        r1.move('d1', 'f3')
        r1.move('f8', 'd6')

        with self.assertRaises(IllegalMoveError):
            r1.move('f3', 'f7')
            
        self.assertTrue(r1.checkmate())


       

        
        
        #TODO test for stale mate (not implemented yet)
        #TODO test for castling (not implemented yet)
        #TODO Testing a game that ends in a draw (insufficient material, threefold repetition, 50 move rule, etc.)
        #TODO test for pawn promotion (not implemented yet)
        #TODO test for en passant (not implemented yet)

        




    


if __name__ == '__main__':
    unittest.main()


tester = TestGame()
tester.test_games()
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



print('TESTING KNIGHT-----------')
knight = Knight('white', 'd4')
print(knight.move('b5'))


print('TESTING QUEEN--------')
queen = Queen('white', 'd4')
print(queen.move('a1'))
print(queen.move('h8'))


print('TESTING KING--------')
king = King('white', 'e4')
print(king.move('e5'))
king2 = King('white', 'a1')
print(king2.move('b2'))


print('TESTING BISHOP--------')
bishop = Bishop('white', 'c4')
print(bishop.move('b3'))
print(bishop.move('g8'))
'''


