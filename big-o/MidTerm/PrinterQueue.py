test_case = int(input())

for i in range(test_case):
  n, m = map(int, input().split())

  q = list(map(int, input().split()))
  q_sort = q[:]
  q_sort.sort()
  
  q_hash = []
  for j in range(len(q)):
    q_hash.append([j, q[j]])

  count = 0
  while True and len(q_hash) > 0:
    tmp = q_hash[0]
    if tmp[0] == m and tmp[1] == q_sort[-1]:
      break
    if tmp[1] != q_sort[-1]:
      q_hash.append(tmp)
    else:
      count += 1
      q_sort.pop()
    q_hash.pop(0)

  print(count + 1)
