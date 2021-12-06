import re

def day2data(filename: str) -> list:
  with open(filename) as input :
      input_list = input.read().strip()
      input_list = re.split('\n| ', input_list)
      input_list = list(map(str,input_list))    
      return input_list
    
day2puzzle = day2data("day2input.txt")

def thirdstar(puzzle : list) -> int:
  crdnt = [0,0]
  lnty = len(puzzle)
  i = 0
  while i < lnty:
    mtype,mvalue = puzzle[i], int(puzzle[i+1])
    match mtype:
      case 'forward': crdnt[0] += mvalue
      case 'down': crdnt[1] += mvalue
      case 'up' : crdnt[1] -= mvalue
    i += 2
  return crdnt[0]*crdnt[1]

thirdstar(day2puzzle)

def fourthstar(puzzle : list) -> int:
  crdnt = [0,0]
  aim = 0
  lnty = len(puzzle)
  i = 0
  while i < lnty:
    mtype,mvalue = puzzle[i], int(puzzle[i+1])
    match mtype:
      case 'forward': 
        crdnt[0] += mvalue
        crdnt[1] += mvalue * aim
      case 'down': 
        aim += mvalue
      case'up': 
        aim -= mvalue
    i += 2
  return crdnt[0]*crdnt[1]

fourthstar(day2puzzle)
