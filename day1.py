def day1data(filename: str) -> list:
  with open(filename) as input :
      input_list = input.read().strip().split("\n")
      input_list = list(map(int,input_list))
      return input_list

day1puzzle = day1data("day1input.txt")

def firststar(puzzle: list) -> int:
  icr = 0
  x = 0
  ln = len(puzzle)
  while x < ln:
    if puzzle[x] > puzzle[x-1] :
      icr +=1
      print(x, end=";") ; print(puzzle[x], end=";") ; print(puzzle[x-1], end=";") ; print(icr)
    x +=1
  return icr

firststar(day1puzzle)

def secondstar(puzzle : list) -> int:
  icr = 0
  x = 0
  ln = len(puzzle)
  while x < ln-3:
    if puzzle[x+3] > puzzle[x] :
      icr +=1
    x +=1
  return icr

secondstar(mypuzzle)
