class Node:
  def __init__(self):
    self.child = dict()
    self.weight = 0

      
def addWord(root, s, weight):
  temp = root
  for ch in s:
    if ch not in temp.child:
      temp.child[ch] = Node()
    if weight > temp.weight:
      temp.weight = weight
    temp = temp.child[ch]

def findWeight(root, s):
  temp = root
  for ch in s:
    if ch not in temp.child:
      return -1
    temp = temp.child[ch]
  return temp.weight

if __name__ == '__main__':
  n, q = map(int, input().split())

  root = Node()
  for i in range(n):
    temp, w = input().split()
    addWord(root, temp, int(w))
  result = []
  for i in range(q):
    temp = input()
    result.append(findWeight(root, temp))
  for i in result:
    print(i)