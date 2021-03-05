parent = []
ranks = []

def makeSet(m):
	global parent, ranks
	parent = [i for i in range(m + 1)]
	ranks = [0 for i in range(m + 1)]

def findSet(u):
  if parent[u] != u:
    parent[u] = findSet(parent[u])
  return parent[u]

def unionSet(u, v):
	up = findSet(u)
	vp = findSet(v)
	if up == vp:
		return
	if ranks[up] > ranks[vp]:
		parent[vp] = up
	elif ranks[up] < ranks[vp]:
		parent[up] = vp
	else:
		parent[up] = vp
		ranks[vp] += 1

if __name__ == '__main__':
  case = 1
  while True:
    [n, m] = map(int, input().split())
    if n == 0 and m == 0:
      break
    parent = []
    ranks = []
    makeSet(n)
    for i in range(m):
      [u, v] = map(int, input().split())
      unionSet(u, v)
    
    religions = {}
    for i in range(n):
      religion = findSet(i + 1)
      if religion not in religions:
        religions[religion] = 1
    
    print("Case {0}: {1}".format(case, len(religions)))
    case += 1
