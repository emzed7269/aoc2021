import re
from statistics import mode

def day3data(filename: str) -> list:
  with open(filename) as input :
      input_list = input.read().strip()
      input_list = re.split('\n| ', input_list)
      input_list = list(map(str,input_list))    
      return input_list
    
day3puzzle = day3data("day3input.txt")

def fifthstar(puzzle : list):
    ln = len(puzzle)
    bits=[[n[i:i+1] for i in range(0,len(n),1)] for n in puzzle]
    lnn = len(bits[0])
    x = 0
    gamma, epsilon=[], []
    while x < lnn:
      md = mode(int(bits[i][x]) for i in range(ln))
      eps = abs(md-1)
      epsilon.append(eps)
      gamma.append(md)
      x += 1
    g, e = '', ''
    for i in gamma:g +=str(i)
    for i in epsilon:e +=str(i)
    g,e = int(g,2), int(e,2)
    return g*e
  
fifthstar(day3puzzle)
