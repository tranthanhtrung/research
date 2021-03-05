class Node:
  def __init__(self):
    self.child = dict()
    self.subset = 0
    self.level = 0

def maxResult(root, s):
  temp = root
  m = 0
  for ch in s:
    if ch not in temp.child:
      temp.child[ch] = Node()
    preLevel = temp.level
    temp = temp.child[ch]
    temp.subset +=  1
    temp.level = preLevel + 1
    if m < temp.subset * temp.level:
      m = temp.subset * temp.level

  return m

if __name__ == '__main__':
  t = int(input())

  result = []
  for i in range(t):
    n = int(input())
    m = 0
    root = Node()
    for j in range(n):
      cur = maxResult(root, input())
      if m < cur:
        m = cur
    result.append(m)

  for i in range(len(result)):
    print('Case ' + str(i + 1) + ':' , result[i])