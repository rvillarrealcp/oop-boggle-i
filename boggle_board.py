import random
import string

class BoggleBoard:
  
  def __init__(self):
    self.board:list = [['_','_','_','_'],['_','_','_','_'],['_','_','_','_'],['_','_','_','_']]
  
  def __str__(self):
    return f"{"".join(self.board[0])}\n{"".join(self.board[1])}\n{"".join(self.board[2])}\n{"".join(self.board[3])}"
  
  def shake(self):
    for i in range(len(self.board)):
      for j in range(len(self.board[i])):
        letter = random.choice(string.ascii_uppercase)
        self.board[i][j] = letter
      print("".join(self.board[i]))
    # for i in range(len(self.board)):
    #   print("".join(self.board[i]))
    return ""

board_setter = BoggleBoard()
print(board_setter)
print(board_setter.shake())
# for i in range(len(board_setter)):
#   letter = random.choice(string.ascii_uppercase)
#   print(letter)
#   board_setter[i] = letter
# print(board_setter)

# row_1 = "".join(board_setter[0:4])
# row_2 = "".join(board_setter[4:8])
# row_3 = "".join(board_setter[8:12])
# row_4= "".join(board_setter[12:])
# new_board = f"{row_1}\n{row_2}\n{row_3}\n{row_4}"
# print(new_board)