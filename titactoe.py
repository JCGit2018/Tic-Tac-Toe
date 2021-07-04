# write your code here



# helper functions
def output_board(selection):
    print("---------")
    print("| " + selection[0] + " " + selection[1] + " " + selection[2] + " |")
    print("| " + selection[3] + " " + selection[4] + " " + selection[5] + " |")
    print("| " + selection[6] + " " + selection[7] + " " + selection[8] + " |")
    print("---------")



def Check_Win(value,selection):
    return (selection[6] == selection[7] == selection[8] == value) or\
           (selection[0] == selection[1] == selection[2] == value) or\
           (selection[3] == selection[4] == selection[5] == value) or\
           (selection[0] == selection[3] == selection[6] == value) or\
           (selection[1] == selection[4] == selection[7] == value) or\
           (selection[2] == selection[5] == selection[8] == value) or\
           (selection[0] == selection[4] == selection[8] == value) or\
           (selection[2] == selection[4] == selection[6] == value)


def board_checker (selection):
    if abs(selection.count('X') - selection.count('O')) >= 2 or Check_Win('X', selection)and\
       Check_Win('O', selection):
       print("Impossible")
    elif Check_Win('X', selection):
       print("X wins")
    elif Check_Win('O', selection):
       print("O wins")
    elif " " in selection:
        return False
    else:
        print("Draw")   
    return True


# The game begins
board = '         '
turn ="X"
output_board(board)
validate_input = '1234567890'
while True:
  coordinates= input("Enter the coordinates: ").split()
  if coordinates[0] not in validate_input or coordinates[1] not in validate_input:
      print("You should enter numbers!")
      continue
  coordinates= [int(number) for number in coordinates]
  if coordinates[0] > 3 or coordinates[1] > 3 or coordinates[0] <= 0  or coordinates[1] <= 0:
      print("Coordinates should be from 1 to 3!")
      continue
  position = (coordinates[0]-1)*3 + coordinates[1]-1

  if board[position] == " ":
      board = board[:position] + turn + board[position+1:]
      output_board(board)
      if turn == "X":
         turn = "O"
      else:
         turn = "X" 
      if board_checker(board):
         break 
  else:
      print('This cell is occupied! Choose another one!')
      
    



