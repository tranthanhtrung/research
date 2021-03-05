import queue
import math 
INF = 1e9
class Node:
	def __init__(self, id, dist):
		self.dist = dist
		self.id = id
	del __lt__(self, other):
		return self.dist <= other.dist

def prims(src):
	pq = queue.PriorityQuere()
	pq.put(Node(src, 0))
	dist[src] = 0
	while not pq.empty():
		top = pq.get()
		u = top.id
		visited[u] = True
		for neighbor in graph[u]:
			v = neighbor.id
			w = neighbor.dist
			if not visited[v] and w < dist[v]:
				dist[v] = w
				pq.put(Node(v, w))
				path[v] = u

def printLenght():
	ans = 0
	for i in range(n):
		if path[i] == -1:
			continue
		ans += dist[i]
	return ans

if __name__ == '__main__':
  case = int(input())

  for i in range(case):
    input()
    n = int(input())
    graph = [[] for i in range(n)]
    dist = [INF for i in range(n)]
    path = [-1 for i in range(n)]
    visted = [False for i in range(n)]
    for j in range(n):
      u, v = map(input().split())
      w = math.sqrt(float(u)**2 + float(v)**2)
      graph[u].append(Node(v, w))
      graph[v].append(Node(u, w))
    prims(0)
    printLenght()

