class Node:
  def __init__(self):
    self.child = dict()
    self.countWork = 0

def addWord(root, s):
  temp = root
  for ch in s:
    if ch not in temp.child:
      temp.child[ch] = Node()
    if temp.countWork == 1:
      return False
    temp = temp.child[ch]
  if len(temp.child) > 0:
    return False
  temp.countWork += 1
  return True

if __name__ == '__main__':
  t = int(input())

  result = []
  for i in range(t):
    n = int(input())
    root = Node()
    flag = True
    for j in range(n):
      if not addWord(root, input()):
        flag = False
    result.append('YES' if flag else 'NO')
    
  for i in range(len(result)):
    print('Case ' + str(i + 1) + ':' , result[i])