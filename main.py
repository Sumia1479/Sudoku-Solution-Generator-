board = [
  [7,8,0,4,0,0,1,2,0],
  [6,0,0,0,7,5,0,0,9],
  [0,0,0,6,0,1,0,7,8],
  [0,0,7,0,4,0,2,6,0],
  [0,0,1,0,5,0,9,3,0],
  [9,0,4,0,6,0,0,0,5],
  [0,7,0,3,0,0,0,1,2],
  [1,2,0,0,0,7,4,0,0],
  [0,4,9,2,0,6,0,0,7]
]

# must pass a full and vaild baored 
def solve(board):
  # find an empty space 
  find = getEmpty(board)
  #if the is no more empty space return true, the boared is solve
  if not find:
    return True
  else:
    # set the row and col to the positions of the empty square (i,j)
    row, col = find
  #check if adding a value between 1-9 at the position of the empty square (row, col) is valid 
  for i in range(1,10):
    #if valid add it into the bored 
    if valid(board, i , (row,col)):
      board[row][col] = i
      #recursivly call solve again with the new board, we will keep trying until we find a solve or we looped through all the possble values 1-9 and none are vaild which then we return false.   
      if solve(board): 
        return True;
      #if there is no vaild solve we will backtrack the last element we just added and try the for loop again with a new value.
      board[row][col] = 0
  return False;
    
def valid(board, num, pos):
  # Check the row that the postion we add the number to lays on  
  for i in range(len(board[0])):
    # Checks every element the row, minus the postion we are looking at, to see if the number we add in the empty postion is present somewhere else in the row. 
    if(board[pos[0]][i] == num and pos[1] != i): 
      return False
    # Checks every element the Col, minus the postion we are looking at, to see if the number we add in the empty postion is present somewhere else in the Col.
    if(board[i][pos[1]] == num and pos[0] != i): 
      return False
  # Check box
  # Finds the box the postion lays in the format of 3x3 grid 
  box_x = pos[1] // 3 # col of the box
  box_y = pos[0] // 3 # row of the box
  # Because box_x and box_y will give us either 0,1, or 2, which is the box the empty square lays on a 3x3 grid, we need to multply by 3, since the position of the actual empty square is on a 9x9 grid, inorder to find the first element in the box and add 3 so we can transverse the whole box
  for i in range(box_y*3, box_y*3 + 3):
     for j in range(box_x*3, box_x*3 + 3):
       if board[i][j]  == num and (i,j) != pos:
         # if all the element in the box is equal to position, excludeing position itself return false 
         return False
  return True
  
  
def displayBoard(board):
  for i in range(len(board)):
    if (i%3 == 0 and i != 0):
      print("- - - - - - - - - - - -")
    for j in range(len(board[i])):
      if( j%3 == 0 and j != 0):
        print(" | ", end="")
      if j == 8:
        print(board[i][j])
      else:
        print(str(board[i][j]) + " ",end="")

# Given a Boared this function find the next empty(0) space and returns the space row and colunm. Loops through the boared to find a space equal to zero
def getEmpty(board): 
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col

    return None


displayBoard(board)
solve(board)
print("________________________")
displayBoard(board)
  
