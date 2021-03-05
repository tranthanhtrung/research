n, max_queue = map(int, input().split())

q = []
processing = 0
result = []
for i in range(n):
  time, duration = map(int, input().split())

  while len(q) != 0 and time >= q[0]:
    q.pop(0)

  if len(q) <= max_queue:
    processing = max(time, processing) + duration
    q.append(processing)
    result.append(processing)
  else:
    result.append(-1)

print(' '.join(str(x) for x in result))