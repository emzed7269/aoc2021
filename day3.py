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

def sixthstar(puzzle : list) -> int:
  bits=[[n[i:i+1] for i in range(0,len(n),1)] for n in puzzle]
  lno2 = len(bits)
  lnco2 = len(bits)
  x, y = 0, 0
  bo2, bco2 = bits, bits
  while lno2 > 1: 
    try :
      modeo2 = mode(int(bo2[i][x]) for i in range(lno2))
    except :
      modeo2 = 1
    bo2 = [i for i in bo2 if int(i[x])== modeo2]
    lno2 = len(bo2)
    x += 1
  while lnco2 > 1:
    try :
      modeco2 = abs(mode(int(bco2[i][y]) for i in range(lnco2))-1)
    except :
      modeco2 = 0
    bco2 = [i for i in bco2 if int(i[y])== modeco2]
    lnco2 = len(bco2)
    y += 1
  o2, co2 = '', ''
  for n in bo2[0]:o2 +=str(n)
  for n in bco2[0]:co2 +=str(n)
  o2, co2 = int(o2,2), int(co2,2)
  return o2*co2

sixthstar(day3puzzle)
