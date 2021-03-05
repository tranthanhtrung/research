q = int(input())

roots = []
graphs = []
for i in range(q):
    [m, n] = list(map(int, input().split()))
    graph = [[] for j in range(m)]
    for j in range(n):
        [r, l] = list(map(int, input().split()))
        graph[r - 1].append(l)
        graph[l - 1].append(r)
    roots.append(int(input()))
    graphs.append(graph)


for i in range(q):
    graph = graphs[i]
    query = []

    visited = [False for j in range(len(graph))]
    path = [0 for j in range(len(graph))]
    q = [roots[i]]
    l = 6
    while len(q) != 0:
        k = q.pop(0)
        visited[k - 1] = True
        
        for j in graph[k - 1]:    
            if visited[j - 1] == False:
                visited[j - 1] = True
                path[j - 1] = path[k - 1] + 1
                q.append(j)

    result = []
    for j in range(len(path)):
        if j == roots[i] - 1:
            continue
        result.append(path[j] * 6 if visited[j] else -1)
        
    
    print(' '.join(str(x) for x in result))
        
