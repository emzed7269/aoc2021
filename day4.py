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
