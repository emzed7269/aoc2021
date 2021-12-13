def day4data(filename: str) -> list:
  with open(filename) as input :
      bingos = input.read().strip()
      bingos = re.split('\n',bingos)
      bingos = list(map(str,bingos))
      order = re.split(',',bingos[0])
      order = [int(i) for i in order]
      bingos = [bingos[n] for n in range(len(bingos)) if n>0 and bingos[n] != '']
      bingos = [re.split(' ',bingos[i]) for i in range(len(bingos))]
      bingos = [[int(bingos[n][i]) for i in range(len(bingos[n])) if bingos[n][i] != ''] for n in range(len(bingos))]
      return order,bingos

day4puzzle = day4data("day4input.txt")

def seventhstar(puzzle: tuple) -> list:
  norder, bingos = puzzle[0], puzzle[1]
  bingos = [bingos[n:n+5] for n in range(0, len(bingos), 5)]
  t = 5
  turn, bingo, lid, winner = [],[],[],[0,1,2]
  winners = [turn, bingo, lid]
  while t < len(norder):
    numbers = norder[:t]
    for b in bingos:
      i = 0
      while i < len(b):
        li = b[i]
        co = [b[j][i] for j in range(len(li))]
        crdnts = [li, co]
        check = all(item in numbers for item in li)
        if check == True:
          winners[0].append(t)
          winners[1].append(bingos.index(b))
          winners[2].append(li)       
        i += 1
    t += 1
  winner[0]=min(winners[0])
  wid = winners[0].index(winner[0])
  numbers=norder[:winner[0]]
  winner[1] = winners[1][wid]
  winner[2] = winners[2][wid]
  first = bingos[winner[1]]
  first=sum(first,[])
  number1=[value for value in first if value in numbers]
  number1=sum([value for value in first if value not in number1])
  number2=numbers[len(numbers)-1]
  return number1*number2
