from piece import Piece, Color
from typing import List
from illegalMoveError import IllegalMoveError

class Queen(Piece):
    # Piece is initialized through colour and current position,(__init__ method in Piece class)

    def __repr__(self):
        return f'Queen(colour= {self.color}, position= {self.current_pos})'


    def __str__(self):
        return f'QUEEN:{self.current_pos}'
    
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
        
     
        a = self.move_diagonally()
        
        
              
        #print(a)
        path = []

        if new_pos in a[0]:
            index = a[0].index(new_pos)
            path = a[0][:index+1]
            return path
            
        elif new_pos in a[1]:
            index = a[1].index(new_pos)
            path = a[1][:index+1]
            return path
            
        elif new_pos in a[2]:
            index = a[2].index(new_pos)
            path = a[2][:index+1]
            return path
            
        elif new_pos in a[3]:
            index = a[3].index(new_pos)
            path = a[3][:index+1]
            return path


        raise IllegalMoveError("this piece can not move in this way (in Queen.py)")
    
    def take():
        pass

    def get_unvalidated_moves(self) -> List[List[str]]:
        x, y = self.current_pos[0], self.current_pos[1]
        x_index = self.cols.index(x)
        y_index = self.rows.index(y)

        #remove the current position from the possible moves
  
        #create our possible_moves array (these are the squares we can move to 
        #if there are no pieces in the way)
    
        

        #if self.color == 'white':
        #    for item in possible_moves:
         #       item.reverse()


        #TODO IMPLEMENT this for all who use this movement pattern.
        b = self.move_forward(8)
        c = self.move_backward(8)
        d = self.move_right(8)
        e = self.move_left(8)
        a = self.move_diagonally()
       
        complete_arr = [b, c, d, e]
       
        complete_arr.extend(a)

        return complete_arr
    

