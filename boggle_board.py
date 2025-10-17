import random

dice = [["A","A","E","E","G","N"],["E","L","R","T","T","Y"],["A","O","O","T","T","W"],["A","B","B","J","O","O"],["E","H","R","T","V","W"],["C","I","M","O","T","U"],["D","I","S","T","T","Y"],["E","I","O","S","S","T"],["D","E","L","R","V","Y"],["A","C","H","O","P","S"],["H","I","M","N","Qu","U"],["E","E","I","N","S","U"], ["E","E","G","H","N","W"],["A","F","F","K","P","S"],["H","L","N","N","R","Z"],["D","E","I","L","R","X"]]


class BoggleBoard:
  
  def __init__(self):
    self.board:list = [['_','_','_','_'],['_','_','_','_'],['_','_','_','_'],['_','_','_','_']]
  
  def __str__(self):
    return "\n".join("  ".join(letter.ljust(2) for letter in row) for row in self.board)
  
  def shake(self):
    dice_idx = 0
    for i in range(len(self.board)):
      for j in range(len(self.board[i])):
        letter = random.choice(dice[dice_idx])
        self.board[i][j] = letter
        dice_idx += 1

board_setter = BoggleBoard()
board_setter.shake()
print(board_setter)
