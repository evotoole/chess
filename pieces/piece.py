from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Literal

class Color(Enum):
    white = 'white'
    black = 'black'

''' board layout  
    white's perspective:
    8
    7
    6
    5
    4
    3
    2
    1
     a b c d e f g h

    black's perspective:
    1
    2
    3
    4
    5
    6
    7
    8
     h g f e d c b a
'''
#by default in white's perspective. flipped if pawn is black.
#the lists should not be mutated, each class should make a copy and store it in __init__
rows = [ '1', '2', '3', '4', '5', '6', '7', '8' ]
cols = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' ]



class Piece(ABC):
    def __init__(self, color: Literal['white', 'black'], current_pos: str):
        self.color = color
        self.current_pos = current_pos
        self.rows = rows if color == 'white' else rows[::-1]
        self.cols = cols if color == 'white' else cols[::-1]

     #takes in a number of steps and returns and array with the cells of the board corresponding 
    #to the steps with respect to the current position
    #TODO: validate moves are in range
    def move_forward(self, num_steps: int) -> List[str]:
        
        x, y = self.current_pos #ex: extracts a, 1 from string 'a1'
        y_index = self.rows.index(y)
        steps: List[str] = []

        for i in range(y_index + 1, y_index + num_steps + 1):
            if -1<i<8:
                steps.append(f'{x}{self.rows[ i ]}')
        steps.reverse()
        return steps
    
    #takes in a number of steps and returns and array with the cells of the board corresponding 
    #to the steps with respect to the current position
    #TODO: validate moves are in range
    def move_left(self, num_steps: int) -> List[str]:
       
        x, y = self.current_pos
        #note that ord('a') - the ACII representation of 'a' has value 97
        x_index = self.cols.index((x))
        steps: List[str] = []
        for j in range(x_index -1 , x_index - num_steps - 1, -1):
            if -1 <j < 8:
                steps.append(f'{self.cols[j]}{y}')
        steps.reverse
        return steps

    #takes in a number of steps and returns and array with the cells of the board corresponding 
    #to the steps with respect to the current position
    #TODO: validate moves are in range
    def move_right(self, num_steps: int) -> List[str]:
    

        x, y = self.current_pos
        #note that ord('a') - the ACII representation of 'a' has value 97
        x_index = self.cols.index(x)
        steps: List[str] = []
        for j in range(x_index +1 , x_index + num_steps + 1):
            if -1 <j < 8:
                steps.append(f'{self.cols[j]}{y}')
        steps.reverse()
        return steps

    #takes in a number of steps and returns and array with the cells of the board corresponding 
    #to the steps with respect to the current position
    #TODO: validate moves are in range
    def move_backward(self, num_steps: int) -> List[str]:
    

        x, y = self.current_pos #ex: extracts a, 1 from string 'a1'
        y_index = self.rows.index(y)
        steps: List[str] = []

        for i in range(y_index -1, y_index - num_steps -1, -1):
            if -1< i < 8:
                steps.append(f'{x}{self.rows[ i ]}')
        steps.reverse()
        return steps
    '''
    - calculates k steps of upper diagonal, and k steps of lower diagonal,
    - starting off from self.current_pos
    '''
    def move_diagonally(self) -> List[List[str]]:

      
        
        x, y = self.current_pos[0], self.current_pos[1]
        x_index = self.cols.index(x)
        y_index = self.rows.index(y)
        #specify size or we get index out of range error

        LU = [] #Left up diagonal
        LD = [] #Left down diagonal
        RU = [] #Right up diagonal
        RD = [] #Right down diagonal

        
        
        tmp1 = x_index
        tmp2 = y_index
       
        while(-1<tmp1<8 and -1<tmp2<8):
            LU.append(f'{self.cols[tmp1]}{self.rows[tmp2]}')
            tmp1 -= 1
            tmp2 += 1
        LU = LU[1:]
        tmp1 = x_index
        tmp2 = y_index
    

        
        while(-1<tmp1<8 and -1<tmp2<8):
            LD.append(f'{self.cols[tmp1]}{self.rows[tmp2]}')
            tmp1 -= 1
            tmp2 -= 1

        LD = LD[1:]
       
        tmp1 = x_index
        tmp2 = y_index
            

       
        while(-1<tmp1<8 and -1<tmp2<8):
            RU.append(f'{self.cols[tmp1]}{self.rows[tmp2]}')
            tmp1 += 1
            tmp2 += 1
        RU = RU[1:]
        tmp1 = x_index
        tmp2 = y_index
    
       
        while(-1<tmp1<8 and -1<tmp2<8):
            RD.append(f'{self.cols[tmp1]}{self.rows[tmp2]}')
            tmp1 += 1
            tmp2 -= 1
        RD = RD[1:]
        tmp1 = x_index
        tmp2 = y_index
        
       
        return [LU,LD,RU,RD]





        '''
        - `idx` indexes the upper diagonal positions.
        - `num_steps + idx` indexes the corresponding lower diagonal positions.
        - Ensures positions are added in the correct order during a single pass.
        '''



        '''
        idx = 0
        for i in range(num_steps, 0, -1):

            left diagonal
            L[ idx ] = f'{self.cols[ x_index - i ]}{self.rows[ y_index + i ]}'

            lower_diag_idx = num_steps - i + 1
            print('lower diag ', self.cols[ x_index + lower_diag_idx ])
            L[ num_steps + idx ] = f'{self.cols[ x_index + lower_diag_idx ]}{self.rows[ y_index - lower_diag_idx ]}'

            right diagonal
            R[ idx ] = f'{self.cols[ x_index + i ]}{self.rows[ y_index + i ]}'

            lower_diag_idx = num_steps - i + 1
            R[ num_steps + idx ] = f'{self.cols[ x_index - lower_diag_idx ]}{self.rows[ y_index - lower_diag_idx ]}'

            idx += 1

        return (L, R)
        '''

    #returns the possivle cells where a piece can move
    @abstractmethod
    def move(self, new_pos: str) -> List[str]:
        pass

    #returns the possible cells where a piece can move to take opponent's piece
    @abstractmethod
    def take(self) -> tuple[ List[str], List[str] ]:
        pass

    @abstractmethod
    def get_unvalidated_moves(self) -> List[str]:
        pass
