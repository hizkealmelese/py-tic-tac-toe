#input correction 
def errorcheck_input(input_str):
  try:
    x = int(input(input_str))
  except:
    print("Invalid Input, Please Try Again")
    x = errorcheck_input(input_str)
    return x
  else:
    return x

import random

#required assets for game
XX = "❌"
OO = "⭕"
X_WIN_GAME = False
O_WIN_GAME = False


gameType = errorcheck_input("[1] Play against Computer | OR | Play against Friend [2]: ")
size = errorcheck_input("game size? : ")

xy = list(range(0,size))
number = list(range(1,size*size+1))
before10 = ["01","02","03","04","05","06","07","08","09"]
turns = 0

#drawing a grid based of size
def graphics():
    grid = [[]]
    count = 0
    for num in number:
        if(num%size)!=0:
            if(num<=9):
              #fix the grid with + "0" so it looks like a square
                grid[count].append("0" + str(num))
            else: grid[count].append(str(num))
        else:
            if(num<=9):
                grid[count].append("0" + str(num))
            else:
                grid[count].append(str(num))
            count = count+1
            grid.append([])
    grid.remove([])
    return(grid)
grid = graphics()

#letting user pick celll
def userPick(PlayerSymbol,PlayerType,ComputerCell):
  global grid
  global number
  global turns
  if(PlayerType=="computer"):
    userCell = ComputerCell
  else: 
    userCell = input("Enter which cell you want to pick: ")
  #no error up in here lol
  Error = True
  while(Error):
    try:
      userCell = int(userCell)
    except:
      userCell = input("Invalid Input; Try again ")
    else:
      if((int(userCell) in number) is False):
        userCell = input("Number cannot be picked; Try again ")
      else: 
        Error = False
        break
  number.remove(userCell)
  turns = turns + 1
  #compute the coordinate from the cell number
  x,y = ((userCell-1)%size),((userCell-1)//size)
  (grid[y])[x] = str(PlayerSymbol)
  return(userCell)

#orginally 
def winCheck():
  winType = ""
  global O_WIN_GAME
  global X_WIN_GAME
  vertical = []
  diagonalTB = []
  diagonalBT = []
  horizontal = []
  vertical = []
  #only run when least possible amount of moves to win achived
  if (turns >= ((2*size)-1)):
    str_numbers = [str(x) for x in number]
    #Diagonal 
    if ((((grid[0])[0]).isdigit()) is False) and (((grid[-1])[-1].isdigit()) is False):
      #top/left---bottom/right
      for i in xy:
        TBnextCell = (grid[i])[i]
        if (TBnextCell.isdigit()) is False:
          diagonalTB.append(TBnextCell)
        else: break
    if ((((grid[-1])[0]).isdigit()) is False) and (((grid[0])[-1].isdigit()) is False):
      #bottem/left---top/right
      for x, y in zip(xy,xy[::-1]):
        BTnextCell = (grid[y])[x]
        if (BTnextCell.isdigit()) is False:
          diagonalBT.append(BTnextCell)
        else: break
          
    #checking the BL-TR list
    if (len(diagonalTB)==size) and ((XX in diagonalTB)is False):
      O_WIN_GAME = True
      winType = "(\\) Diagonal"
    if (len(diagonalTB)==size) and ((OO in diagonalTB)is False):
      X_WIN_GAME = True
      winType = "(\\) Diagonal"

    #checking the TL-BR
    if (len(diagonalBT)==size) and ((XX in diagonalBT)is False):
      O_WIN_GAME = True
      winType = "(//) Diagonal"
    if (len(diagonalBT)==size) and ((OO in diagonalBT)is False):
      X_WIN_GAME = True
      winType = "(//) Diagonal"
      
    for row in grid:
      #stop loop if win happens
      if (X_WIN_GAME is True) or (O_WIN_GAME is True):
        break
      #check if any number in row, then check if row is fully X or O
      if (any(num in row for num in before10) or any(num in row for num in str_numbers)) is False:
        #horizontal 
        if(XX in row) is False:
          O_WIN_GAME = True
          winType = "Horizontal"
          horizontal = row
          break
        if(OO in row) is False:
          X_WIN_GAME = True
          winType = "Horizontal"
          horizontal = row
          break
      #vertical 
      
      #vertical code is TERRIBLE, I KNOW 
      #try to make it into a function next time but does it really matter?
      #because uses the amount of lines calling said fuction for XX and OO anyway
      else:
        for cell in row:
          # X vertical check
          if (cell is XX):
            for y in range(0,(size)):
              verticalNextCell = grid[y][row.index(cell)]
              if (verticalNextCell is XX):
                vertical.append(verticalNextCell)
              if ((verticalNextCell is XX) is False):
                vertical = []
            if(len(vertical)==size) and (cell is XX):
              X_WIN_GAME = True
              winType = "Vertical"

          # O verical check 
          if (cell is OO):
            for y in range(0,(size)):
              verticalNextCell = grid[y][row.index(cell)]
              if (verticalNextCell is OO):
                vertical.append(verticalNextCell)
              if ((verticalNextCell is OO) is False):
                vertical = []
            if(len(vertical)==size) and (cell is OO):
              O_WIN_GAME = True
              winType = "Vertical"

  
  return(winType,("X", X_WIN_GAME),("O", O_WIN_GAME)) #debugging-> # ,
      #   ("horizontal", horizontal),
      #   ("vertical", vertical),
      #   ("//", diagonalBT),
      #   ("\\", diagonalTB))


def Computer(Player):
  PlayerCell = int(Player)
  CenterCell = ((size*size)/2)+0.5
  #compute the coordinate from the last picked player cell number
  player_x,player_y = ((PlayerCell-1)%size),((PlayerCell-1)//size)
  
  #create a function for -,|,\\,// line checks
  # \\ Check
  def TopLeft_BottomRight_Diagonal_Check():
    diagonal_count = 0
    possibleCells = []
    for i in xy:
      nextCell = grid[i][i]
      if (nextCell.isdigit()):
        possibleCells.append(nextCell)
      if (nextCell == XX):
        diagonal_count = diagonal_count + 1
  #return the amount of XX in that specific line, and the remaining available cells on that line]
    return [diagonal_count,possibleCells,"\\"]
  # // Check
  def TopRight_BottomLeft_Diagonal_Check():
    diagonal_count = 0
    possibleCells = []
    for x, y in zip(xy,xy[::-1]):
      nextCell = (grid[y])[x]
      if (nextCell.isdigit()):
        possibleCells.append(nextCell)
      if (nextCell == XX):
        diagonal_count = diagonal_count + 1
    return [diagonal_count,possibleCells,"//"]
  # || check
  def Vertical_Check():
    vertical_count = 0
    possibleCells = []
    for i in xy:
      nextCell = grid[i][player_x]
      if (nextCell == XX):
        vertical_count = vertical_count + 1
      if (nextCell.isdigit()):
        possibleCells.append(nextCell)
    return [vertical_count,possibleCells,"||"]
  # -- check
  def Horizontal_Check():
    horizontal_count = (grid[player_y]).count(XX)
    possibleCells = []
    for nextCell in grid[player_y]:
      if (nextCell.isdigit()):
        possibleCells.append(nextCell)
    return [horizontal_count,possibleCells,"--"]

  
  FullCheck = [TopLeft_BottomRight_Diagonal_Check(),TopRight_BottomLeft_Diagonal_Check(),Vertical_Check(),Horizontal_Check()]

  #most critical lines are put in front
  FullCheck.sort(reverse=True)
    
  #THE LINE DELETION TOOL IS BAD, IT TAKES 2 LOOPS 
  #the idea is to check if the cell list is empty and delete any lines without avaliable cells, but it needs to run before and during computer pick. this is because it will not delete a line if there are >1 lines with no cells BUT it will go out of range if there only 1 line if i use range(len(fullcheck)) because it is one extra element 

  for i in FullCheck:
    if [] in i:
      FullCheck.remove(i)
  #fuction to let computer pick a cell
  def ComputerPick():
    
    #if there are no lines available, pick a random cell
    if([] in FullCheck[0]) and ([] in FullCheck[-1]):
      userPick(OO,"computer",random.choice(number))
      return 0
      
    #delete any remaining empty lines if still are inside list
    for i in FullCheck:
      if [] in i:
        FullCheck.remove(i)
        
    #find the critical number amount based on size
    if(size%2)==0: 
      CriticalNumber = int(size/2)
    if(size%2)!=0:
      CriticalNumber = int((size/2)+0.5)
    
    #check the first line of fullcheck has achived the critical number 
    #if so,extract the possible cells in that line and pick a cell.
    if(int(FullCheck[0][0]) >= CriticalNumber):
      MostCritical = (FullCheck[0][1])[0]
      userPick(OO,"computer",MostCritical)
      return 0  
      
    #if not,pick the least critical line and pick a cell
    else:
      LeastCritical = (FullCheck[-1][1])[0]
      userPick(OO,"computer",LeastCritical)
      return 0

  if(size%2)!=0:
    if(CenterCell in number):
      #if center cell is available then let computer pick it since it is the best cell
      userPick(OO,"computer",int(CenterCell))
    else:
      ComputerPick()
  else:
    ComputerPick()
  
  return Player, FullCheck
  
      
while any([X_WIN_GAME,O_WIN_GAME]) is False:
  print(winCheck())
  print(number)
  user = userPick(XX,"",0)
  for i in grid:
    print(i)
    print("\n")
  print("\n")
  print(Computer(user))
  print("\n")
  print(winCheck())
  print("*"*50)
  for i in grid:
    print(i)
    print("\n")
  print("*"*50)