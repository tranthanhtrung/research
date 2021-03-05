n = int(input())




for i in range(n):
  s = input()
  graph = [[1 if x == 'Y' else -1 for x in s]]
  for j in range(1, len(s)):
    tmp = []
    for k in input():
      tmp.append(1 if k == 'Y' else -1)
    graph.append(tmp)
  
