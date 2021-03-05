[n, w] = list(map(int, input().split()))
a = list(map(int, input().split()))

a.sort()
result = min(a[0], a[n]/2.0)*3*n

print(min(w, result))
