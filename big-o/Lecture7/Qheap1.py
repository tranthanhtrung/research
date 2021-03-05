import queue

n = int(input())

result = []
m_heap = queue.PriorityQueue()

for i in range(n):
  line = list(map(int, input().split()))

  if len(line) == 1:
    m = m_heap.get()
    result.append(m)
    m_heap.put(m)
  elif line[0] == 1:
    m_heap.put(line[1])
  else:
    m_heap.remove(line[1])

for i in result:
  print(i)