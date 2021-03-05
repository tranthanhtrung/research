n = int(input())
matrix = []
rL = 10000000000
rR = 0
for i in range(0, n):
    matrix.append(list(map(int, input().split())))

for i in range(0, n):
    if i == 0:
        rL = matrix[i][0]
        rR = matrix[i][1]
    else:
        rL = rL if rL < matrix[i][0] else matrix[i][0]
        rR = rR if rR > matrix[i][1] else matrix[i][1]

cover = -1
for i in range(0, n):
    if matrix[i] == [rL, rR]:
        cover = i + 1
print(cover)
