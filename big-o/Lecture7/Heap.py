import queue

n = int(input())
arr = list(map(int, input().split()))

mHeap = queue.PriorityQueue()

class PQEntry:
  def __init__(self, value):
    self.value = value
  def __lt__(self, other):
    return self.value > other.value

result = []
for i in range(n):
  mHeap.put(PQEntry(arr[i]))
  if i <= 1:
    result.append(-1)
  else:
    biggest = mHeap.get()
    s_biggest = mHeap.get()
    t_biggest = mHeap.get()
    result.append(biggest.value * s_biggest.value * t_biggest.value)
    mHeap.put(biggest)
    mHeap.put(s_biggest)
    mHeap.put(t_biggest)

for i in result:
  print(i)
    