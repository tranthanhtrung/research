k,n,w = map(int, input().split())
r = int(k*(1+w)*w/2)

print(r - n if r - n > 0 else 0)