class Node:
  def __init__(self):
    self.count = 0
    self.child = dict()

def addNumber(root, number):
  temp = root
  for ch in number:
    if ch not in temp.child:
      temp.child[ch] = Node()
    temp = temp.child[ch]
    if temp.count != 0:
      return False
  temp.count += 1
  if len(temp.child) != 0:
    return False
  return True

if __name__ == '__main__':
  cases = int(input())

  for i in range(cases):
    n = int(input())
    isPos = True
    root = Node()
    for j in range(n):
      if not addNumber(root, input()):
        isPos = False
    
    print('YES' if isPos else 'NO')