[n, minutes] = list(map(int, input().split()))
time = list(map(int, input().split()))

max_read = 0
read = 0
j = 0

for i in range(n):
    while minutes < time[i]:
        minutes += time[j]
        j += 1
        read -= 1
    
    minutes -= time[i]
    read += 1
    max_read = max(max_read, read)

print(max_read)
