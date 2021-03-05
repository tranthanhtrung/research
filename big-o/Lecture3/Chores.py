[n, a, b] = list(map(int, input().split()))
arr = list(map(int, input().split()))

arr.sort()

print(arr[b] - arr[b-1])