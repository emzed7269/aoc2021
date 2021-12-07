#def sixthstar(puzzle : list) -> int:
#    ln = len(puzzle)
#    bits=[[n[i:i+1] for i in range(0,len(n),1)] for n in puzzle]
#    lnn = len(bits[0])
#    x = 0
#    gamma, epsilon=[], []
#    while x < lnn:
#      md = mode(int(bits[i][x]) for i in range(ln))
#      eps = abs(md-1)
#      mylist = [bits[i] for i in range(ln) if int(bits[i][x])==md]
#      x += 1
#      print(md)
#      print(mylist)
#bits=[[n[i:i+1] for i in range(0,len(n),1)] for n in puzzle]
class oxygen:
  def __init__(s,puzzle,oxend):
    s.puzzle=puzzle
    s.ln=len(puzzle)
    s.bits=[[n[i:i+1] for i in range(0,len(n),1)] for n in s.puzzle]
    s.lnn=len(s.bits[0])
    s.oxend=oxend 
    s.x = 0
  def __iter__(s):
    return s
  def __next__(s):
    if s.ln == s.oxend: raise StopIteration
    md = mode(int(s.bits[i][s.x]) for i in range(s.ln))
    s.puzzle = [s.bits[i] for i in range(s.ln) if int(s.bits[i][s.x])==md]
    print(s.ln)
    print(s.bits)
    print(s.lnn)
    print(s.oxend)
    return s.puzzle
    s.x += 1

oxg = oxygen(day3puzzle,1)
iterox = iter(oxg)
print(next(oxg))
print(next(oxg))
