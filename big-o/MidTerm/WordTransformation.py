n = int(input())
_ = input()

def check_str(str1, str2):
  if len(str1) != len(str2):
    return False
  for i in str1:
    if str2.find(i) != -1:
      str1 = str1.replace(i,'',1)
      str2 = str2.replace(i,'',1)
  return len(str1) == 1 and len(str2) == 1

def prepare_map(arr):
  map_b = [[] for i in arr]
  for i in range(len(arr)):
    for j in range(i, len(arr), 1):
      if check_str(arr[i],arr[j]):
        map_b[i].append(j)
        map_b[j].append(i)
  return map_b

def BFF(arr, root):
  path = [-1 for i in arr]
  dis = [False for i in arr]
  q = [root]
   
  while len(q) > 0:
    tmp = q.pop(0)
    if path[tmp] != -1:
      for i in arr[tmp]:
        if path[i] != -1:
          path[i] = tmp
          a
  return path



for i in range(n):
  arr = []
  while True:
    tmp = input()
    if tmp == '*':
      break
    else:
      arr.append(tmp)

  out = []
  while True:
    tmp = input()
    if len(tmp) == 0:
      break
    out.append(tmp.split())
  print(prepare_map(arr))

  # for j in out:
  #   q_out = j[0]
  #   path = [-1 for i in hash_work]
  #   while len(q_out) > 0:
  #     tmp = q_out.pop()
  #     if path[q]
  